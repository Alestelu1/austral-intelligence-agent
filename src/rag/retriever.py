"""Chunked keyword retrieval with phrase boosting."""

import re
from collections import Counter

from src.rag.document_loader import Document


STOPWORDS = {
    "para",
    "como",
    "desde",
    "hasta",
    "entre",
    "sobre",
    "donde",
    "cuando",
    "cual",
    "cuál",
    "cómo",
    "qué",
    "que",
    "los",
    "las",
    "una",
    "uno",
    "unos",
    "unas",
    "del",
    "por",
    "con",
    "sin",
    "más",
    "muy",
    "esta",
    "este",
    "estas",
    "estos",
}


def normalize_terms(text: str) -> list[str]:
    """Return normalized searchable terms."""
    return [
        word
        for word in re.findall(r"\b[\wáéíóúñü]+\b", text.lower())
        if len(word) > 2 and word not in STOPWORDS
    ]


def split_document(
    document: Document,
    chunk_size: int = 900,
    overlap: int = 150,
) -> list[Document]:
    """Split a document into overlapping text chunks."""
    text = document.content.strip()

    if len(text) <= chunk_size:
        return [document]

    chunks: list[Document] = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append(
                Document(
                    source=document.source,
                    page=document.page,
                    content=chunk_text,
                )
            )

        if end == len(text):
            break

        start = max(end - overlap, start + 1)

    return chunks


def score_document(question: str, document: Document) -> float:
    """Calculate weighted relevance between a question and a chunk."""
    question_terms = normalize_terms(question)
    document_terms = normalize_terms(document.content)

    if not question_terms or not document_terms:
        return 0.0

    question_counts = Counter(question_terms)
    document_counts = Counter(document_terms)

    score = 0.0

    for term, question_frequency in question_counts.items():
        frequency = document_counts.get(term, 0)

        if frequency:
            score += question_frequency * min(frequency, 4)

    normalized_question = " ".join(question_terms)
    normalized_document = " ".join(document_terms)

    if normalized_question in normalized_document:
        score += 18.0

    if len(question_terms) >= 2:
        for index in range(len(question_terms) - 1):
            phrase = " ".join(question_terms[index : index + 2])

            if phrase in normalized_document:
                score += 6.0

    source_name = document.source.lower()

    for term in question_terms:
        if term in source_name:
            score += 1.5

    unique_matches = len(set(question_terms).intersection(document_terms))
    coverage = unique_matches / len(set(question_terms))
    score += coverage * 8.0

    return score


def retrieve_documents(
    question: str,
    documents: list[Document],
    limit: int = 3,
    minimum_score: float = 5.0,
) -> list[Document]:
    """Return the most relevant document chunks."""
    chunks = [
        chunk
        for document in documents
        for chunk in split_document(document)
    ]

    scored_chunks = [
        (score_document(question, chunk), chunk)
        for chunk in chunks
    ]

    relevant_chunks = [
        (score, chunk)
        for score, chunk in scored_chunks
        if score >= minimum_score
    ]

    relevant_chunks.sort(
        key=lambda item: (
            item[0],
            item[1].source,
            item[1].page or 0,
        ),
        reverse=True,
    )

    selected: list[Document] = []
    seen: set[tuple[str, int | None, str]] = set()

    for _, chunk in relevant_chunks:
        key = (
            chunk.source,
            chunk.page,
            chunk.content[:120],
        )

        if key in seen:
            continue

        seen.add(key)
        selected.append(chunk)

        if len(selected) >= limit:
            break

    return selected