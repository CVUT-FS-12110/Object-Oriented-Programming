
import streamlit as st
import requests

# Streamlit UI
st.title("API Fetch Example in Streamlit")

# Input for API
api_url = st.text_input("Enter API URL", "http://127.0.0.1:8000/temperature")

if st.button("Fetch Data"):
    try:
        # Fetch API data
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Display JSON response
        data = response.json()
        st.write("API Response:", data)

        # Example: Display specific part of the JSON
        st.write("Temperature Data:", data["temperature"][1])

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching API: {e}")