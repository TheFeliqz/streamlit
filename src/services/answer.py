import os
from dotenv import load_dotenv

from components.llm_call import llm_response
from components.llm_call import llm_embedding
from components.vector_store import find_chunks_in_vector_store

# load .env variables
load_dotenv()

def answer(question):
    question_embedding = llm_embedding([question], model=os.getenv("EMBEDDING_MODEL"))

    closest_chunks = find_chunks_in_vector_store(question_embedding)

    prompt = ""
    for i, chunk in enumerate(closest_chunks, start=1):
        prompt += f"Information {i}:\n{chunk}\n\n"
    prompt += f"Question:\n{question}"

    instructions = "Answer the following question with only the information given to you. Do not make up any facts and do not include new information. If you dont have enough information to answer, say so. Answer in the language the question is written in."
    response = llm_response(prompt=prompt, model=os.getenv("LLM_MODEL_ANSWER"), instructions=instructions)

    return response
