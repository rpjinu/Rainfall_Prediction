import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open(r'C:\Users\Ranjan kumar pradhan\.vscode\rainfall_prediction\rainfall_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Rainfall Prediction App")

st.header("Enter Weather Parameters:")
# Input fields for user
pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1010.0, step=0.1)
dewpoint = st.number_input("Dewpoint (°C)", min_value=-20.0, max_value=40.0, value=15.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
cloud = st.number_input("Cloud Cover (%)", min_value=0, max_value=100, value=50)
sunshine = st.number_input("Sunshine Duration (hours)", min_value=0.0, max_value=24.0, value=5.0, step=0.1)
winddirection = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, value=90.0, step=1.0)
windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, value=10.0, step=0.1)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'pressure': [pressure],
    'dewpoint': [dewpoint],
    'humidity': [humidity],
    'cloud': [cloud],
    'sunshine': [sunshine],
    'winddirection': [winddirection],
    'windspeed': [windspeed]
})

# Prediction
if st.button("Predict Rainfall"):
    prediction = model.predict(input_data)
    result = "Rainfall is likely" if prediction[0] == 1 else "No Rainfall"
    st.subheader(f"Prediction: {result}")
