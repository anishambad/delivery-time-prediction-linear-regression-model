import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model_dummies.pkl", "rb") as f:
    model_dummies = pickle.load(f)

st.title("🚚 Delivery Time Prediction")

# Numeric inputs
distance = st.number_input("Distance (km)", min_value=0.0, step=0.1)
prep_time = st.number_input("Preparation Time (minutes)", min_value=0, step=1)
experience = st.number_input("Courier Experience (years)", min_value=0, step=1)

# Dropdowns for categorical features
weather = st.selectbox("Weather", ["Clear", "Foggy", "Rainy", "Snowy", "Windy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])

# Prediction button
if st.button("Predict Delivery Time"):
    # Build input dictionary with dummy columns
    input_dict = {
        "Distance_km": [distance],
        "Preparation_Time_min": [prep_time],
        "Courier_Experience_yrs": [experience],
        "Weather_Clear": [1 if weather == "Clear" else 0],
        "Weather_Foggy": [1 if weather == "Foggy" else 0],
        "Weather_Rainy": [1 if weather == "Rainy" else 0],
        "Weather_Snowy": [1 if weather == "Snowy" else 0],
        "Weather_Windy": [1 if weather == "Windy" else 0],
        "Traffic_Level_High": [1 if traffic == "High" else 0],
        "Traffic_Level_Low": [1 if traffic == "Low" else 0],
        "Traffic_Level_Medium": [1 if traffic == "Medium" else 0],
        "Time_of_Day_Afternoon": [1 if time_of_day == "Afternoon" else 0],
        "Time_of_Day_Evening": [1 if time_of_day == "Evening" else 0],
        "Time_of_Day_Morning": [1 if time_of_day == "Morning" else 0],
        "Time_of_Day_Night": [1 if time_of_day == "Night" else 0],
        "Vehicle_Type_Bike": [1 if vehicle == "Bike" else 0],
        "Vehicle_Type_Car": [1 if vehicle == "Car" else 0],
        "Vehicle_Type_Scooter": [1 if vehicle == "Scooter" else 0],
    }

    # Convert to DataFrame
    input_df = pd.DataFrame(input_dict)

    # Predict
    prediction = model_dummies.predict(input_df)[0]
    st.success(f"Predicted Delivery Time: {prediction:.2f} minutes")
