from sentence_transformers import SentenceTransformer

def embed(chunks, embedding_model):
    model = SentenceTransformer(embedding_model)
    numpy_embeddings = model.encode(chunks)
    list_embeddings = numpy_embeddings.tolist()

    return list_embeddings
