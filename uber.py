import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the pre-trained model
model = joblib.load('uber_model.pkl')  # Adjust the path to where your model is saved

# Define a function to make predictions
def make_prediction(lat, lon, weekday, hour):
    input_features = np.array([[lat, lon, weekday, hour]])
    prediction = model.predict(input_features)
    return prediction

# Streamlit app
st.title("Uber Trip Prediction")

# Create input fields for prediction
lat = st.slider("Latitude", min_value=-90.0, max_value=90.0, value=40.75)
lon = st.slider("Longitude", min_value=-180.0, max_value=180.0, value=-73.95)
weekday = st.slider("Weekday", min_value=0, max_value=6, value=0)
hour = st.slider("Hour", min_value=0, max_value=23, value=0)

# Make prediction
if st.button("Predict"):
    prediction = make_prediction(lat, lon, weekday, hour)
    st.write(f"Predicted Base: {prediction[0]}")
