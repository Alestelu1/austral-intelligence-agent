"""Load local Markdown and PDF documents for the RAG pipeline."""

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


MARKDOWN_DIR = Path("data/documents")
PDF_DIR = Path("data/raw/pdf")


@dataclass(frozen=True)
class Document:
    """Representation of a documentary unit."""

    source: str
    content: str
    page: int | None = None


def load_markdown_documents(
    directory: Path = MARKDOWN_DIR,
) -> list[Document]:
    """Load Markdown files from the configured directory."""
    if not directory.exists():
        return []

    documents: list[Document] = []

    for path in sorted(directory.glob("*.md")):
        content = path.read_text(encoding="utf-8").strip()

        if content:
            documents.append(
                Document(
                    source=path.name,
                    content=content,
                )
            )

    return documents


def load_pdf_documents(
    directory: Path = PDF_DIR,
) -> list[Document]:
    """Load PDF files as one document unit per page."""
    if not directory.exists():
        return []

    documents: list[Document] = []

    for path in sorted(directory.glob("*.pdf")):
        reader = PdfReader(path)

        for page_number, page in enumerate(reader.pages, start=1):
            content = (page.extract_text() or "").strip()

            if content:
                documents.append(
                    Document(
                        source=path.name,
                        page=page_number,
                        content=content,
                    )
                )

    return documents


def load_all_documents() -> list[Document]:
    """Load every supported local source."""
    return load_markdown_documents() + load_pdf_documents()