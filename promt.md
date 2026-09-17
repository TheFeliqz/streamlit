I am building a little streamlit application, where a friend gave me the following assignment:

- Seite 1 – Dokument zusammenfassen: Dokument hochladen und über "summarize()" zusammenfassen lassen.
  Keywords: Document Upload, Summarization, LLM

- Seite 2 – Wissensbasis aufbauen und befragen: Mehrere Handbücher nacheinander über "ingest()" einlesen. Anschließend können Fragen über ein Textfeld gestellt und über "answer()" mithilfe eines LLMs beantwortet werden.
  Keywords: RAG, Ingestion, Chunking, Embeddings, Vector Store, Retrieval, LLM

Erweiterte Ausprägung: Anstelle der direkt in die Streamlit-Anwendung eingebetteten Funktionen summarize, ingest und answer wird eine separate FastAPI-Schicht bereitgestellt. Diese stellt die Endpunkte /summarize, /ingest und /answer bereit, mit denen die Streamlit-Anwendung kommuniziert.

END OF ASSIGNMENT

Dont assume what errors i am getting or what i want to do next. ask if you are unsure. Just answer to what I am saying.

I have implemented "Seite 1" fully. Here is the code. Do not go into any comments, just take the code as given. I also have attached a picture of the project sturcture. 

app.py:
import streamlit as st

st.title ("Document Summary")


pages = [
    st.Page("pages/1_summarize.py", title="Summarize"),
    st.Page("pages/2_knowledgebase.py", title="Knowledge Base")
]

navigation = st.navigation(pages)
navigation.run()


summarize.py:
import os
from openai import OpenAI
from services.llm_call import llm_call

def summarize(text):
    # Check text length, if too long: chunk it (e.g. >10000 Words)

    instructions = "I want you to summarize the following text. Do not make up any facts and do not include new information, only summarize the given information."

    response = llm_call(prompt=text, model="summarize", instructions=instructions)

    return response

llm_call.py:
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
        model = os.getenv("MODEL_SUMMARIZE")
    elif model == "answer_question":
        model = os.getenv("MODEL_ANSWER_QUESTION")
    else:
        model = None

    response = client.responses.create(
        model = os.getenv(model),
        instructions = instructions,
        input = prompt,
    )

    return response.output_text # this has to be a string


END OF CODE 

Task:
Analysze the code and give feedback only for implementation of Page 1. After that (clearly mark where) outline ideas for Seite 2. Explain the keywords given in the task (conceptually, not in context of my task) 