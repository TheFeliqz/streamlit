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
def llm_call(prompt, model, instructions):
    if model == "summarize":
        model = os.getenv("LLM_MODEL_SUMMARIZE")
    elif model == "answer":
        model = os.getenv("LLM_MODEL_ANSWER")
    else:
        model = None

    response = client.responses.create(
        model = os.getenv(model),
        instructions = instructions,
        input = prompt,
    )

    return response.output_text # returns LLM answer as a string
