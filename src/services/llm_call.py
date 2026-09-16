import os
from openai import OpenAI
from dotenv import load_dotenv


# load .env variables
load_dotenv()


# client to call the api
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)


# function to call api and get response
def llm_call(prompt, instructions):
    response = client.responses.create(
        model = os.getenv("MODEL_SUMMARIZE"),
        instructions = instructions,
        input = prompt,
    )

    return response.output_text # this has to be a string
