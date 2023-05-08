from dotenv import load_dotenv
import os
import streamlit as st
import openai
import pinecone

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_KEY")

# Set up Pinecone API credentials
pinecone.init(api_key=os.environ.get("PINECONE_KEY"),
              environment='northamerica-northeast1-gcp')

# Define Pinecone vector index and dimensions
index_name = "chatbot-index"
dimensions = 768

# Initialize Pinecone vector index if not exists
if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, dimension=dimensions)

# Define function to generate OpenAI GPT-3 responses


def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define Streamlit app


def app():
    st.title("Chatbot")

    # Get user input
    user_input = st.text_input("You: ")

    # Convert user input to a float if possible, otherwise use the input as is
    try:
        user_input = float(user_input)
    except ValueError:
        pass

    # Store user preferences in Pinecone vector index
    if user_input:
        # Generate OpenAI GPT-3 response
        prompt = f"User: {user_input}\nChatbot:"
        response = generate_response(prompt)
        if isinstance(user_input, str):
            id = user_input
        else:
            id = str(user_input)
        vector = [float(x) for x in response.split("\n")[0].split()]
        pinecone.upsert(index_name=index_name, ids=[id], vectors=[vector])
        # Retrieve similar user preferences from Pinecone vector index
        if response == "I don't know.":
            query = pinecone.query(index_name=index_name,
                                query_vectors=[vector], top_k=5)
            if query.ids:
                st.write("Similar user preferences:")
                for id in query.ids:
                    st.write(id)

        # Display chatbot response
        st.text_area("Chatbot:", value=response, height=200, max_chars=2048)

# Run Streamlit app
if __name__ == "__main__":
    app()
