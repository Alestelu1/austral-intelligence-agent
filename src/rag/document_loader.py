"""Load local Markdown documents for the future RAG pipeline."""

from dataclasses import dataclass
from pathlib import Path


DOCUMENTS_DIR = Path("data/documents")


@dataclass(frozen=True)
class Document:
    """Representation of a local documentary source."""

    source: str
    content: str


def load_markdown_documents(
    directory: Path = DOCUMENTS_DIR,
) -> list[Document]:
    """Load all Markdown files from the configured directory."""
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