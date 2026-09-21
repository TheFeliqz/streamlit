def chunk(text, chunk_size, chunk_overlap):

    chunks = []

    if len(text) <= chunk_size:
        return [text]

    start = 0
    while len(text) - start > chunk_overlap:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - chunk_overlap

    return chunks
