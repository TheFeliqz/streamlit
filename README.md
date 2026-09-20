# Document Processor

A small Streamlit app for summarizing documents and building a searchable knowledge base with retrieval-augmented Q&A.

## Features

**Page 1 — Summarize**
Upload a document and summarize its content.

**Page 2 — Knowledge Base**
Ingest multiple documents into a vector store (ChromaDB), then ask questions about this information.

## Setup

Create a `.env` file (recommendations for models is given):

```env
OPENAI_API_KEY=sk-...

LLM_MODEL_SUMMARIZE=gpt-5-nano
LLM_MODEL_ANSWER=gpt-5-nano

EMBEDDING_MODEL=text-embedding-3-small
```

**Run locally:**
```bash
pip install -r requirements.txt
streamlit run src/app.py
```

**Run with Docker:**
```bash
docker-compose up --build
```

## Future Ideas

- implement with FastAPI 
- change ChromaDB to store data in persistent memory or cloud https://docs.trychroma.com/docs/run-chroma/clients
- let the user select a difficulty/complexity of own question, internally changing the number of chunks used for answering the question (e.g. easy, medium, hard)
- delete button to clear ingested files

last updated: 20.09.2026
