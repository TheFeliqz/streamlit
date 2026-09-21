import os
from dotenv import load_dotenv

from backend.components.llm_call import llm_response
from backend.components.llm_call import llm_embedding
from backend.components.vector_store import find_chunks_in_vector_store

# load .env variables
load_dotenv()

def answer(question, complexity):
    question_embedding = llm_embedding([question], model=os.getenv("EMBEDDING_MODEL"))

    if complexity == "Easy":
        number_of_chunks = 2
    elif complexity == "Medium":
        number_of_chunks = 5
    elif complexity == "Hard":
        number_of_chunks = 10

    closest_chunks = find_chunks_in_vector_store(question_embedding, number_of_chunks)

    prompt = ""
    for i, chunk in enumerate(closest_chunks, start=1):
        prompt += f"Information {i}:\n{chunk}\n\n"
    prompt += f"Question:\n{question}"

    instructions = "Answer the following question with only the information given to you. Do not make up any facts and do not include new information. If you dont have enough information to answer, say so. Answer in the language the question is written in."
    response = llm_response(prompt=prompt, model=os.getenv("LLM_MODEL_ANSWER"), instructions=instructions)

    return response
