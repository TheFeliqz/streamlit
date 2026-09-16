import os
from openai import OpenAI
from call_llm import call_llm

def summarize(text):

    # Check text length, if too long: chunk it

    promt = f"""
        I want you to summarize the following text. Do not make up any facts and do not include new information, only summarize the given information.
        
        Text:
        {text}
    """

    response = call_llm(promt)

    # repose -> string

    return response

    # send to llm
    
    # write response

