from components.llm_embedding import llm_embedding

def embed(chunks, embedding_model):
    return llm_embedding(chunks,embedding_model)

# this file exists because I wanted to do the embedding another way, but it didnt work