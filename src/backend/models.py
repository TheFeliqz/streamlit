from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    file_text: str

class SummarizeResponse(BaseModel):
    summary: str

# Ingest is handled in main.py directly since it processes multipart/form-data and not a JSON

# Clear Vector Store is a DELETE Request

class AnswerRequest(BaseModel):
    question_text: str
    complexity: str

class AnswerResponse(BaseModel):
    answer: str
