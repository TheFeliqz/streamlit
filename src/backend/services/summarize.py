import os
from dotenv import load_dotenv

from components.llm_call import llm_response

# load .env variables
load_dotenv()

def summarize(text, summary_length):
    instructions = f"I want you to summarize the following text. Do not make up any facts and do not include new information, only summarize the given information. Answer in the language the text is written in. Length of the summary (interpret the number as number of words or percent of original text): {summary_length}."

    response = llm_response(prompt=text, model=os.getenv("LLM_MODEL_SUMMARIZE"), instructions=instructions)

    return response
