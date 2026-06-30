# Document Analyzer Chatbot

A starter Python project for a document analyzer chatbot built with FastAPI and designed for future GenAI enhancements such as LLMs, RAG, and agentic workflows.

## Features
- FastAPI health and chat endpoints
- Document upload endpoint
- Ready for LLM and RAG integration

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
pytest -q
```
