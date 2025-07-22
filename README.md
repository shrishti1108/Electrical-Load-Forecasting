⚡ Electrical Load Forecasting & Energy Optimization (Green AI)
A region-specific electric load forecasting app that combines AI-based prediction with real-time energy-saving recommendations. Built using Prophet, Random Forest, and Streamlit, this project promotes sustainable consumption through interpretable and lightweight modeling.

🌍 Overview
India’s growing electricity demands make forecasting regional load crucial for grid stability and sustainability. This project helps visualize short-term load trends and offers actionable tips to reduce unnecessary power use — a step toward energy-efficient, Green AI solutions.

🚀 Features
📊 Region-wise hourly electric load forecasting
🔮 Prophet-based time series modeling
🌡️ Weather-integrated model with monthly temperature correlation
📈 Random Forest baseline for comparison
✅ MAE, RMSE, and R² metrics
💡 Dynamic energy-saving recommendations
🧠 Green AI compliant: lightweight, interpretable, sustainable
🌐 Streamlit frontend for user interaction

🔧 Installation
Clone the repository:
git clone https://github.com/your-username/Electrical-Load-Forecasting.git
cd Electrical-Load-Forecasting
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run streamlit_app.py
Ensure the datasets are in the path:
./Dataset/hourlyLoadDataIndia.xlsx
./Dataset/monthly_temp.xlsx
🧠 Models Used
Model	Description
Prophet	For trend/seasonality decomposition and forecasting
Random Forest	Baseline supervised learning comparison
🧩 Green AI Approach
✅ Low-compute models (Prophet ≠ deep learning)
✅ Regional selection avoids overtraining
✅ Encourages real-world energy efficiency
✅ Transparent + interpretable forecasting
📌 Future Enhancements
 Real-time weather API integration
 Daily retraining with new load data
 Mobile-friendly dashboard
 Deploy on Streamlit Cloud
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
Jupyter Notebook
99.7%
 
Python
0.3%
Suggested workflows
Based on your tech stack
Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
Python Package using Anaconda logo
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
More workflows
