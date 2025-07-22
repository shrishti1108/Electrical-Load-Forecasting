# ⚡ Electrical Load Forecasting & Energy Optimization (Green AI)

A region-specific electric load forecasting app that combines AI-based prediction with real-time energy-saving recommendations. Built using **Prophet**, **Random Forest**, and **Streamlit**, this project promotes sustainable consumption through interpretable and lightweight modeling.

---

## 🌍 Overview

India’s growing electricity demands make forecasting regional load crucial for grid stability and sustainability. This project helps visualize short-term load trends and offers actionable tips to reduce unnecessary power use — a step toward energy-efficient, Green AI solutions.

---

## 🚀 Features

- 📊 **Region-wise hourly electric load forecasting**
- 🔮 **Prophet-based time series modeling**
- 🌡️ **Weather-integrated model** with monthly temperature correlation
- 📈 **Random Forest baseline** for comparison
- ✅ Evaluation metrics: **MAE**, **RMSE**, **R²**
- 💡 **Dynamic energy-saving recommendations**
- 🧠 **Green AI compliant**: lightweight, interpretable, sustainable
- 🌐 **Streamlit frontend** for real-time user interaction

---

## 📁 Project Structure

```
Electrical-Load-Forecasting/
│
├── Dataset/
│ ├── hourlyLoadDataIndia.xlsx # Hourly load per region
│ └── monthly_temp.xlsx # Monthly avg. temperature
│
├── Load Forecast.ipynb # Notebook with model training & results
├── streamlit_app.py # Streamlit UI
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```



---

## 🔧 Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/your-username/Electrical-Load-Forecasting.git
cd Electrical-Load-Forecasting
```
Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
Step 3: Run the Streamlit app

```
streamlit run streamlit_app.py
```
🧠 Models Used
Model	Description
Prophet	Time series model for trend/seasonality forecasting
Random Forest	Baseline supervised ML model for comparison

🧩 Green AI Approach

✅ Low-compute models (no deep learning)

✅ Region-specific modeling to avoid overfitting

✅ Promotes real-world energy efficiency

✅ Fully interpretable and transparent predictions

📌 Future Enhancements
🌦️ Real-time weather API integration

🔁 Daily retraining with updated load data

📱 Mobile-friendly dashboard

☁️ Deploy on Streamlit Cloud for easy access



