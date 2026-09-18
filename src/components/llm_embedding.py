import os
from openai import OpenAI
from dotenv import load_dotenv

# load .env variables
load_dotenv()

client = OpenAI()

def llm_embedding(chunks, model):
    response = client.embeddings.create(
        input=chunks,
        model=model
    )

    embeddings = [result.embedding for result in response.data]

    return embeddings
