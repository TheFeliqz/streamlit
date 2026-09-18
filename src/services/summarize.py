import os
from dotenv import load_dotenv

from components.llm_response import llm_response

# load .env variables
load_dotenv()

def summarize(text):
    instructions = "I want you to summarize the following text. Do not make up any facts and do not include new information, only summarize the given information. Answer in the language the text is written in."

    response = llm_response(prompt=text, model=os.getenv("LLM_MODEL_SUMMARIZE"), instructions=instructions)

    return response
