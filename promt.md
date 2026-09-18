I am building a little streamlit application, where a friend gave me the following assignment:

- Seite 1 – Dokument zusammenfassen: Dokument hochladen und über "summarize()" zusammenfassen lassen.
  Keywords: Document Upload, Summarization, LLM

- Seite 2 – Wissensbasis aufbauen und befragen: Mehrere Handbücher nacheinander über "ingest()" einlesen. Anschließend können Fragen über ein Textfeld gestellt und über "answer()" mithilfe eines LLMs beantwortet werden.
  Keywords: RAG, Ingestion, Chunking, Embeddings, Vector Store, Retrieval, LLM

Erweiterte Ausprägung: Anstelle der direkt in die Streamlit-Anwendung eingebetteten Funktionen summarize, ingest und answer wird eine separate FastAPI-Schicht bereitgestellt. Diese stellt die Endpunkte /summarize, /ingest und /answer bereit, mit denen die Streamlit-Anwendung kommuniziert.

END OF ASSIGNMENT

Dont assume what errors i am getting or what i want to do next. ask if you are unsure. Just answer to what I am saying.

I have implemented "Seite 1" fully. Here is the code. Do not go into any comments, just take the code as given. I also have attached a picture of the project sturcture. 


app.py:



END OF CODE 

Task for you:
...