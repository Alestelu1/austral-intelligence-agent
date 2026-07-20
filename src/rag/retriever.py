"""Simple keyword-based retrieval for local documents."""

import re

from src.rag.document_loader import Document


def normalize_text(text: str) -> set[str]:
    """Convert text into a normalized set of searchable terms."""
    return {
        word
        for word in re.findall(r"\b\w+\b", text.lower())
        if len(word) > 3
    }


def retrieve_documents(
    question: str,
    documents: list[Document],
    limit: int = 3,
) -> list[Document]:
    """Return the most relevant documents using keyword overlap."""
    question_terms = normalize_text(question)

    scored_documents: list[tuple[int, Document]] = []

    for document in documents:
        document_terms = normalize_text(document.content)
        score = len(question_terms.intersection(document_terms))

        if score > 0:
            scored_documents.append((score, document))

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        document
        for _, document in scored_documents[:limit]
    ]