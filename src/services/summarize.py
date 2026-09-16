import os
from dotenv import load_dontev
from openai import OpenAI

def summarize(text, summarization_length):
    promt = f"""
        I want you to summarize the following text. Do not make up any facts, just summarize the given information.
        
        Text:
        {text}
    """

    # send to llm
    
    # write response
