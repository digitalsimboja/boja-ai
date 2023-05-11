from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message
import openai
import pinecone

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_KEY")

# Set up Pinecone API credentials
pinecone.init(api_key=os.environ.get("PINECONE_KEY"),
              environment='northamerica-northeast1-gcp')


def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text if response.choices else ''


st.title("Evveland Self-service ")
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input(
        "You", "Welcome, how may I help you today?", key="user_input")
    return input_text


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i],
                is_user=True, key=str(i) + '_user')
