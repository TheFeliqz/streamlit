import os
from openai import OpenAI

from services.chunk import chunk

# function gets a list of file objects
def ingest(files):

    for file in files:

        # chunk parameters
        chunk_size = 1000
        chunk_overlap = 250

        # chunk text of the current file
        file_text = file.getvalue().decode("utf-8")
        chunks = chunk(file_text, chunk_size, chunk_overlap)

        for text in chunks:
            pass
            # embed chunk (sentence-transformers; )

            # store chunk (text + embedding) in vector store (chromadb)
