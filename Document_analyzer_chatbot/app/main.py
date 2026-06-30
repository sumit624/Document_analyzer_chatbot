from typing import List

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.config import settings
from app.rag import rag_store
from app.services import AnswerService

app = FastAPI(title=settings.app_name, version="0.2.0")
answer_service = AnswerService()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    return {"status": "ok", "llm_provider": settings.llm_provider}


@app.post("/documents/upload", response_model=dict)
async def upload_documents(files: List[UploadFile] = File(...)):
    uploaded = []
    for file in files:
        contents = await file.read()
        text = contents.decode("utf-8", errors="ignore")
        rag_store.add_document(file.filename, text)
        uploaded.append(file.filename)
    return {"documents_uploaded": len(uploaded), "filenames": uploaded}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return ChatResponse(answer=answer_service.answer(req.message))
