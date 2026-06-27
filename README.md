# 🚚 Delivery Time Prediction App

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)

Welcome to the **Delivery Time Prediction App** 🎉  
This project is an interactive **Streamlit web application** that predicts delivery time based on multiple real‑world factors such as distance, preparation time, courier experience, weather, traffic, time of day, and vehicle type.  

The underlying model is a **Linear Regression** trained on encoded features and achieves an accuracy of ~81%.  
It’s designed to showcase an end‑to‑end ML workflow — from preprocessing and training to deployment with Streamlit.

---

## ✨ Features
- 📊 **Accurate Predictions** – Predicts delivery time in minutes using a regression model.  
- 🎛️ **Interactive UI** – Numeric inputs and dropdowns for categorical features.  
- 🌦️ **Realistic Factors** – Weather, traffic, time of day, and vehicle type included.  
- 🌐 **Streamlit Powered** – Clean, responsive web interface.  

---

## 📂 Project Structure
delivery-time-predictor/
│
├── app.py                # Streamlit UI
├── model_dummies.pkl     # Trained regression model
├── requirements.txt      # Dependencies
├── README.md             # Project overview
└── .gitignore            # Ignore unnecessary files

## 🚀 Getting Started

### 
1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/delivery-time-predictor.git
cd delivery-time-predictor

2️⃣ Install dependencies
bash
pip install -r requirements.txt

3️⃣ Run the app
bash
streamlit run app.py

🛠️ Tech Stack

🐍 Python
📦 Pandas
📈 Scikit-learn
🌐 Streamlit

📈 Model Details 

Algorithm: Linear Regression
Training: Encoded categorical + numeric features
Accuracy: ~81%

👤 Author
Built by Anish — Third‑year Computer Engineering student at SPPU, passionate about data science, analytics, and machine learning.


