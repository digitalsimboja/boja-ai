# Inspiration

The inspiration for this project came from the desire to create a smarter and more efficient search engine that can deliver more accurate and relevant results to users.

## What it does

This AI-powered search engine uses natural language processing and machine learning algorithms to understand the user's query and provide personalized results based on their search history, preferences, and context.

## How I built it

This project was built using Python, Flask, and a variety of open-source libraries, including TensorFlow, Keras, NumPy, Pandas, and spaCy. The application uses Pinecone vector databases and OpenAI's GPT-3 API for semantic search and natural language processing.

## Challenges I ran into

One of the main challenges was integrating the Pinecone vector databases and OpenAI's GPT-3 API into the application and ensuring that they work seamlessly together. There were also challenges around optimizing the machine learning models and ensuring that the search engine is scalable and can handle a large volume of queries.

## Accomplishments that I am proud of

One of the biggest accomplishments of this project is the ability to deliver highly personalized and accurate search results to users. Another accomplishment is the integration of cutting-edge AI technologies into the application, which makes it more intelligent and efficient.

## What I learned

Through building this project, I learned a lot about natural language processing, machine learning algorithms, and how to integrate AI technologies into web applications. I also learned about the importance of data quality and the role it plays in the accuracy and relevance of search results.

## Built With

    Python
    Flask
    TensorFlow
    Keras
    NumPy
    Pandas
    spaCy
    Pinecone vector databases
    OpenAI's GPT-3 API

## Setup

Create a virtual environment and activate it

```
python3 -m venv ai
source ai/bin/activate
```

Clone the repository

```
git clone https://github.com/digitalsimboja/boja-ai.git
cd boja-ai
```

## Installation

Install the dependencies:

```
pip install -r requirements.txt
```

## Run the app

```
streamlit run src/app.py
```
