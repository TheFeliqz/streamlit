Entwickle eine kleine Streamlit-Applikation

DONE - Seite 1 – Dokument zusammenfassen: Dokument hochladen und über "summarize()" zusammenfassen lassen.
  Keywords: Document Upload, Summarization, LLM

- Seite 2 – Wissensbasis aufbauen und befragen: Mehrere Handbücher nacheinander über "ingest()" einlesen. Anschließend können Fragen über ein Textfeld gestellt und über "answer()" mithilfe eines LLMs beantwortet werden.
  Keywords: RAG, Ingestion, Chunking, Embeddings, Vector Store, Retrieval, LLM

Erweiterte Ausprägung: Anstelle der direkt in die Streamlit-Anwendung eingebetteten Funktionen summarize, ingest und answer wird eine separate FastAPI-Schicht bereitgestellt. Diese stellt die Endpunkte /summarize, /ingest und /answer bereit, mit denen die Streamlit-Anwendung kommuniziert.


.env needs
OPENAI_API_KEY=...
LLM_MODEL_SUMMARIZE=gpt-5-nano
LLM_MODEL_ANSWER=gpt-5-nano
EMBEDDING_MODEL=google/embeddinggemma-300m

