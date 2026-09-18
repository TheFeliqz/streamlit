import chromadb
import uuid

client = chromadb.Client()  #TODO add db in persistent memory https://docs.trychroma.com/docs/run-chroma/clients
collection = client.create_collection(name="manuals", embedding_function=None)

def store_in_vector_store(chunks, embeddings):
    collection.add(
        ids = [str(uuid.uuid4()) for _ in chunks],
        documents=chunks,
        embeddings=embeddings
    )
