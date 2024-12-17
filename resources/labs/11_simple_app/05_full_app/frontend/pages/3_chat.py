import streamlit as st
from openai import OpenAI

# Streamlit app title
st.title("Groq Chat - LLaMA/Mixtral Model Integration")

# Sidebar API Key input
if "groq_api_key" not in st.session_state:
    st.session_state["groq_api_key"] = st.secrets["GROQ_API_KEY"]

# Initialize OpenAI-compatible client for Groq
if st.session_state["groq_api_key"]:
    client = OpenAI(
        api_key=st.session_state["groq_api_key"], 
        base_url="https://api.groq.com/openai/v1"
    )
else:
    st.warning("Please enter your Groq API key to continue.")
    st.stop()

# Initialize chat model and messages
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-8b-8192"  # Default model, replace with valid Groq model name

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input for chat
if prompt := st.chat_input("What do you want to ask?"):
    # Append user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call the Groq API for the assistant's response
    with st.chat_message("assistant"):
        try:
            # Stream Groq's response
            stream = client.chat.completions.create(
                model=st.session_state["groq_model"],
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True
            )
            # Stream response content
            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {e}")

