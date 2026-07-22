"""Streamlit entry point for Austral Intelligence Agent."""

import streamlit as st

from src.services.gemini_service import generate_answer
from src.rag.document_loader import load_all_documents
from src.rag.retriever import retrieve_documents


st.set_page_config(
    page_title="Austral Intelligence Agent",
    page_icon="🧭",
    layout="centered",
)

st.title("🧭 Austral Intelligence Agent")
st.caption("Challenge Alura ONE / AI for Tech")

st.success(
    "MVP documental operativo con Gemini, recuperación local "
    "y citas por fuente y página."
)

question = st.text_area(
    "Escribe una consulta",
    placeholder=(
        "Ejemplo: ¿Qué importancia tiene Puerto Williams "
        "para la conectividad austral de Chile?"
    ),
)

if st.button("Consultar", type="primary"):
    clean_question = question.strip()

    if not clean_question:
        st.warning("Escribe una consulta antes de continuar.")
    else:
        try:
            with st.spinner("Analizando la consulta..."):
                documents = load_all_documents()

                relevant_documents = retrieve_documents(
                    clean_question,
                    documents,
                )

                context = "\n\n".join(
                    f"Fuente: {document.source}\n{document.content}"
                    for document in relevant_documents
                )

                answer = generate_answer(
                    clean_question,
                    context=context,
                )

            st.subheader("Respuesta documental")
            st.write(answer)

            if relevant_documents:
                st.subheader("Fuentes recuperadas")

                displayed_sources: set[tuple[str, int | None]] = set()

                for document in relevant_documents:
                    source_key = (document.source, document.page)

                    if source_key in displayed_sources:
                        continue

                    displayed_sources.add(source_key)

                    if document.page is not None:
                        st.write(
                            f"- `{document.source}`, página {document.page}"
                        )
                    else:
                        st.write(f"- `{document.source}`")
                else:
                 st.warning(
                    "No se encontraron documentos relevantes "
                    "en la colección local."
                )

        except RuntimeError as error:
            st.error(str(error))

        except Exception:
            st.error(
                "No fue posible procesar la consulta. "
                "Revisa la conexión, la configuración y los documentos."
            )

st.divider()

st.caption(
    "Las respuestas documentales futuras mostrarán fuentes y reconocerán "
    "cuando no exista evidencia suficiente."
)

              