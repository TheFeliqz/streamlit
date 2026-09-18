import os
from dotenv import load_dotenv

from components.chunk import chunk
from components.embed import embed
from components.store_in_vector_store import store_in_vector_store

# load .env variables
load_dotenv()

# function gets a list of file objects
def ingest(files):

    for file in files:
        file_text = file.getvalue().decode("utf-8")

        chunk_size = 1000
        chunk_overlap = 250

        chunks = chunk(file_text, chunk_size, chunk_overlap)  # returns a list of strings (chunks of text)

        embeddings = embed(chunks, embedding_model=os.getenv("EMBEDDING_MODEL"))  # returns a list of lists (vectors)

        store_in_vector_store(chunks, embeddings)
