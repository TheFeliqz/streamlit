import os
from openai import OpenAI
from services.llm_call import llm_call

def answer(question):
    # embed the question


    # find embeddings/vectors from the vector store that are closest to the question (e.g. 5 closest)
    

    # retrieve text from those closest embeddings/vectors from vector store and store them in a good format in prompt variable
    prompt = ""


    # hardcoded instructions and calling the llm with all the information needed to answer the given question
    instructions = instructions = "Answer the following Question with only the information given to you in this prompt. Do not make up any facts and do not include new information. Answer in the language the question is written in."
    response = llm_call(prompt=prompt, model="answer", instructions=instructions)

    return response
