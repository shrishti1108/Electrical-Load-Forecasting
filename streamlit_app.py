
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

st.set_page_config(page_title="Electric Load Forecast + Recommendations", layout="wide")

@st.cache_data
def load_data():
    load_df = pd.read_excel("Dataset/hourlyLoadDataIndia.xlsx")
    temp_df = pd.read_excel("Dataset/monthly_temp.xlsx")
    load_df['datetime'] = pd.to_datetime(load_df['datetime'])
    load_df['year'] = load_df['datetime'].dt.year
    load_df['month'] = load_df['datetime'].dt.month
    temp_df['month'] = pd.to_datetime(temp_df['Month'], format='%b').dt.month
    temp_df['Year'] = temp_df['Year'].astype(int)
    temp_df = temp_df.rename(columns={'Year': 'year'})
    return pd.merge(load_df, temp_df, on=['year', 'month'], how='left')

df = load_data()

region_map = {
    "National": "National Hourly Demand",
    "North": "Northen Region Hourly Demand",
    "West": "Western Region Hourly Demand",
    "East": "Eastern Region Hourly Demand",
    "South": "Southern Region Hourly Demand",
    "North-East": "North-Eastern Region Hourly Demand"
}

st.title("🔌 Region-Wise Electric Load Forecasting + Efficiency Tips")
selected_region = st.selectbox("🌍 Select Region", list(region_map.keys()))
target_column = region_map[selected_region]

df_region = df[['datetime', target_column]].rename(columns={
    'datetime': 'ds',
    target_column: 'y'
})

# Prophet Forecasting
model = Prophet(daily_seasonality=True, yearly_seasonality=True)
model.fit(df_region)
future = model.make_future_dataframe(periods=48, freq='H')
forecast = model.predict(future)

# Plot forecast (safe rendering)
st.subheader(f"📈 Forecast for {selected_region} Region")
fig1 = model.plot(forecast)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.clf()

# Plot components (safe rendering)
st.subheader("🧩 Trend and Seasonality")
fig2 = model.plot_components(forecast)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.clf()

# Evaluation
merged = pd.merge(df_region, forecast[['ds', 'yhat']], on='ds')
mae = mean_absolute_error(merged['y'], merged['yhat'])
rmse = np.sqrt(mean_squared_error(merged['y'], merged['yhat']))

st.subheader("📉 Forecast Accuracy")
st.write(f"**MAE**: {mae:.2f}")
st.write(f"**RMSE**: {rmse:.2f}")

# Recommendation Logic
def get_energy_recommendation(load_value):
    if load_value > 160000:
        return "⚠️ Extremely High Load — Suggest industrial load shifting, avoid peak hour usage."
    elif load_value > 140000:
        return "🔺 High Load — Encourage public to reduce AC use and turn off idle devices."
    elif load_value > 120000:
        return "🟡 Moderate Load — Promote LED bulbs, avoid unnecessary daytime lighting."
    else:
        return "🟢 Normal Load — Maintain standard energy use."

predicted_load = forecast.iloc[-1]['yhat']
recommendation = get_energy_recommendation(predicted_load)

st.subheader("💡 Energy Efficiency Recommendation")
st.write(f"Predicted Load (Next Hour): **{predicted_load:,.2f} MW**")
st.success(recommendation)
