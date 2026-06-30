from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class DocumentChunk:
    content: str
    source: str


@dataclass
class RAGStore:
    documents: List[DocumentChunk] = field(default_factory=list)

    def add_document(self, filename: str, text: str) -> None:
        chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]
        for chunk in chunks:
            self.documents.append(DocumentChunk(content=chunk, source=filename))

    def search(self, query: str, top_k: int = 3) -> List[DocumentChunk]:
        query_lower = query.lower()
        scored = []
        for doc in self.documents:
            score = sum(1 for term in query_lower.split() if term in doc.content.lower())
            if score:
                scored.append((score, doc))
        scored.sort(reverse=True)
        return [doc for _, doc in scored[:top_k]]


rag_store = RAGStore()
