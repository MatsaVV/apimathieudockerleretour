import streamlit as st
import requests

# Title of the Streamlit web app
st.title('Iris Flower Prediction App')

# Input fields for user to enter data
sepal_width = st.number_input('Sepal Width', min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input('Petal Length', min_value=0.0, max_value=10.0, value=4.0)
petal_width = st.number_input('Petal Width', min_value=0.0, max_value=10.0, value=1.5)

if st.button('Predict'):
    # Define the API endpoint (replace with your actual FastAPI URL)
    api_url = 'https://<yourwebappname>.azurewebsites.net/predict'  # Replace with your actual FastAPI URL

    # Create the payload to send to the API
    payload = {
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    # Send the request to the FastAPI server
    response = requests.post(api_url, json=payload)

    # Process the response from the API
    if response.status_code == 200:
        result = response.json()
        st.success(f"The predicted sepal length is: {result['predicted_sepal_length']}")
    else:
        st.error("Failed to get a prediction from the API")

# Optionally, a fun endpoint to test connection to FastAPI
if st.button('Quentin Hero'):
    api_url_quentin = 'https://<yourwebappname>.azurewebsites.net/quentin'  # Replace with your actual FastAPI URL
    response = requests.get(api_url_quentin)
    if response.status_code == 200:
        result = response.json()
        st.success(result['message'])
    else:
        st.error("Failed to connect to the /quentin endpoint")
