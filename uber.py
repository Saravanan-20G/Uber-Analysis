import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Streamlit app configuration - This should be the first Streamlit command
st.set_page_config(page_title="Uber Trip Base Predictor", layout="wide")

# Custom CSS for background image and styling
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://www.lifewire.com/thmb/dtWznG83C1mW-tWf0nsb1fj8xHg=/5000x3337/filters:no_upscale():max_bytes(150000):strip_icc()/young-man-holds-a-smart-device-while-using-uber-app-858492232-5b32d1884cedfd0037f8117a.jpg"); 
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff; /* Text color for headers */
}

.stButton>button {
    background-color: #007bff; /* Primary button color */
    color: #ffffff; /* Button text color */
    border-radius: 10px;
}

.stNumberInput label, .stSelectbox label, .stSlider label, .stTextInput label {
    color: #00FF00; /* Label text color */
}

.stNumberInput input, .stSelectbox div, .stSlider>div, .stTextInput input {
    background-color: #f0f8ff; /* Light background for inputs */
    color: #000000; /* Input text color */
}

.sidebar .sidebar-content {
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent sidebar background */
    color: #ffffff; /* Sidebar text color */
}

.stMarkdown {
    color: #FF69B4; /* Light text color for markdown */
}

.stSubheader, .stText {
    color: #FFD700; /* Text color for subheader and other text */
}
</style>
'''

# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the pre-trained model
model = load('uber_model.pkl')

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
