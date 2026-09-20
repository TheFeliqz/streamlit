import chromadb
import uuid

client = chromadb.Client()
collection = client.get_or_create_collection(name="manuals", embedding_function=None)

def store_in_vector_store(chunks, embeddings):
    collection.add(
        ids = [str(uuid.uuid4()) for _ in chunks],
        documents=chunks,
        embeddings=embeddings
    )

def find_chunks_in_vector_store(question_embedding, number_of_chunks):
    closest_chunks = collection.query(
        query_embeddings=question_embedding,
        n_results=number_of_chunks
    )

    return closest_chunks["documents"][0]
