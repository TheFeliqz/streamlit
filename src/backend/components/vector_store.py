import chromadb
import uuid

client = chromadb.PersistentClient()
collection = client.get_or_create_collection(name="manuals", embedding_function=None)

def store_in_vector_store(chunks, embeddings, name):
    collection.add(
        ids = [str(uuid.uuid4()) for _ in chunks],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"file_name": name} for _ in chunks]
    )

def find_chunks_in_vector_store(question_embedding, number_of_chunks):
    closest_chunks = collection.query(
        query_embeddings=question_embedding,
        n_results=number_of_chunks
    )

    return closest_chunks["documents"][0]

def clear_vector_store():
    if collection.count() == 0:
        pass
    else:
        collection.delete(ids=collection.get()["ids"])
