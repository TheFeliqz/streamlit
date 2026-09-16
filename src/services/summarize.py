import os
from openai import OpenAI
from services.llm_call import llm_call

def summarize(text):
    # Check text length, if too long: chunk it (e.g. >10000 Words)

    instructions = "I want you to summarize the following text. Do not make up any facts and do not include new information, only summarize the given information."

    response = llm_call(prompt=text, instructions=instructions)

    return response
