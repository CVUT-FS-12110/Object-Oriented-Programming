import streamlit as st
import numpy as np
import pandas as pd
import time
import requests

st.set_page_config(
    page_title="Graph",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",

)

# Input for API
api_url = st.text_input("Enter API URL", "http://127.0.0.1:8000/temperature_list")
api_post = "http://127.0.0.1:8000/temperature"

if st.button("Fetch Data"):
    try:
        # Fetch API data
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Display JSON response
        data = response.json()
        st.write("API Response:", data)

        # Use Pandas DataFrame to process it
        df = pd.DataFrame(data["temperature"], columns=["Index", "Temperature"]).set_index("Index")

        # Example: Display specific part of the JSON
        st.write(data["temperature"])

        chart = st.line_chart(df)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching API: {e}")


# post temperature data to api using button
temperature = st.number_input("Enter Temperature", value=0.0)
if st.button("Post Temperature"):
    try:
        params = {"temperature": temperature}  # Query parameter
        response = requests.post(api_post, params=params)    


        response.raise_for_status()  # Raise exception for HTTP errors

        # Display JSON response
        data_response = response.json()
        st.write("API Response:", data_response)

    except requests.exceptions.RequestException as e:
        st.error(f"Error posting API: {e}")

# delete button for deleting last data
if st.button("Delete Last Data"):
    try:
        response = requests.delete(api_post)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Display JSON response
        data_response = response.json()
        st.write("API Response:", data_response)

    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting API: {e}")

# print(type(data))
# print(data.size)
# print(data)



# for i in range(1, 30):
#     data = pd.DataFrame(data.values + np.random.randn(1),columns=["data"])
#     print(type(data))
#     print(data.size)
#     print(data)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(data)
#     progress_bar.progress(i)
#     last_rows = data
#     time.sleep(0.5)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")