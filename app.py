"""Streamlit entry point for Austral Intelligence Agent."""

import streamlit as st

from src.services.gemini_service import generate_answer
from src.rag.document_loader import load_markdown_documents
from src.rag.retriever import retrieve_documents


st.set_page_config(
    page_title="Austral Intelligence Agent",
    page_icon="🧭",
    layout="centered",
)

st.title("🧭 Austral Intelligence Agent")
st.caption("Challenge Alura ONE / AI for Tech")

st.info(
    "Primera versión con Gemini. El corpus documental y la recuperación "
    "RAG todavía se encuentran en construcción."
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
                documents = load_markdown_documents()

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

                for document in relevant_documents:
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