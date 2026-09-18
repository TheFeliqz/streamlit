from sentence_transformers import SentenceTransformer

def embed(chunks, embedding_model):
    model = SentenceTransformer(embedding_model)
    numpy_embeddings = model.encode(chunks)
    list_embeddings = numpy_embeddings.tolist()

    return list_embeddings

#TODO add distinction that allow not only "encode" but separate between document and query (store and question)
# see: https://huggingface.co/google/embeddinggemma-300m