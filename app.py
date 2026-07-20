"""Streamlit entry point for Austral Intelligence Agent."""

import streamlit as st

from src.services.gemini_service import generate_answer


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
                answer = generate_answer(clean_question)

            st.subheader("Respuesta preliminar")
            st.write(answer)

            st.warning(
                "Esta respuesta aún no ha sido contrastada con el corpus "
                "documental del proyecto."
            )

        except RuntimeError as error:
            st.error(str(error))

        except Exception:
            st.error(
                "No fue posible comunicarse con Gemini. "
                "Revisa la API key, la conexión y la configuración del modelo."
            )

st.divider()

st.caption(
    "Las respuestas documentales futuras mostrarán fuentes y reconocerán "
    "cuando no exista evidencia suficiente."
)