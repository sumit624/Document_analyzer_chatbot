from __future__ import annotations

from app.rag import rag_store


class AnswerService:
    def answer(self, message: str) -> str:
        matches = rag_store.search(message)
        if not matches:
            return (
                "No relevant documents were found yet. Upload a document and ask a question "
                "about its contents."
            )

        context = "\n".join(f"- {m.content} (source: {m.source})" for m in matches)
        return (
            "Based on the uploaded documents, here is a concise answer:\n"
            f"{context}\n\n"
            f"User question: {message}"
        )
