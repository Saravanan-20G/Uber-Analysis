import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model
model = load('uber_model.pkl')

# Streamlit app configuration
st.set_page_config(page_title="Uber Trip Base Predictor", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Prediction"])

if page == "Home":
    # Home page content
    st.title("Welcome to the Uber Trip Base Predictor")
    st.write("""
        ## About the Project
        This application predicts the base location for Uber trips based on features like latitude, longitude, 
        weekday, and hour of the trip. The model was trained using historical Uber trip data and can provide 
        predictions in real-time based on user inputs.
        
        ### How to Use the Predictor
        Navigate to the "Prediction" page using the sidebar. Enter the trip details, and the application will 
        provide the predicted base location.
    """)

elif page == "Prediction":
    # Prediction page content
    st.title("Uber Trip Base Predictor")
    st.write("Enter the details of the Uber trip to get the predicted base location.")

    # Input features
    lat = st.number_input('Latitude', format="%.6f", key='lat_input')
    lon = st.number_input('Longitude', format="%.6f", key='lon_input')
    weekday = st.selectbox('Weekday', list(range(7)), key='weekday_selectbox')
    hour = st.slider('Hour', 0, 23, key='hour_slider')

    # Button to trigger prediction
    if st.button('Predict Base'):
        # Create input dataframe
        input_data = pd.DataFrame({
            'Lat': [lat],
            'Lon': [lon],
            'Weekday': [weekday],
            'Hour': [hour]
        })

        
        # Predict the base
        prediction_encoded = model.predict(input_data)

        # Ensure the prediction is an integer
        prediction_index = int(prediction_encoded[0])

        # Decode the prediction
        base_names = ['Base1', 'Base2', 'Base3', 'Base4']  # Modify as per your actual base names
        prediction = base_names[prediction_index]

        # Display the prediction
        st.subheader("Predicted Base Location")
        st.write(prediction)

