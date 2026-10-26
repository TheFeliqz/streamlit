# src/backend/main.py
from fastapi import FastAPI, UploadFile

from models import SummarizeRequest, SummarizeResponse, AnswerRequest, AnswerResponse
from services.summarize import summarize
from services.ingest import ingest
from services.answer import answer
from components.vector_store import clear_vector_store

app = FastAPI()


@app.post("/summarize", response_model=SummarizeResponse)
def api_summarize(request: SummarizeRequest):
    return SummarizeResponse(summary = summarize(request.file_text, request.summary_length))


@app.post("/ingest")
def api_ingest(files: list[UploadFile]):
    ingest(files)
    return {"status": "ok"}


@app.delete("/clear_vector_store")
def api_clear_vector_store():
    clear_vector_store()
    return {"status": "ok"}


@app.post("/answer", response_model=AnswerResponse)
def api_answer(question: AnswerRequest):
    return AnswerResponse(answer=answer(question.question_text, question.complexity))

