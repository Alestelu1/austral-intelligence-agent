"""Streamlit entry point for Austral Intelligence Agent."""

import streamlit as st


st.set_page_config(
    page_title="Austral Intelligence Agent",
    page_icon="🧭",
    layout="centered",
)

st.title("🧭 Austral Intelligence Agent")
st.caption("Challenge Alura ONE / AI for Tech")

st.info(
    "MVP en construcción. La primera versión incorporará consultas sobre una "
    "colección documental controlada del extremo austral de Chile."
)

question = st.text_area(
    "Escribe una consulta",
    placeholder="Ejemplo: ¿Qué fuentes describen la conectividad de Puerto Williams?",
)

if st.button("Consultar", type="primary"):
    if not question.strip():
        st.warning("Escribe una consulta antes de continuar.")
    else:
        st.warning(
            "El motor de recuperación todavía no está conectado. "
            "Esta interfaz confirma que el esqueleto inicial funciona."
        )
        st.write("**Consulta registrada:**", question.strip())

st.divider()
st.caption(
    "Las respuestas futuras deberán mostrar fuentes y reconocer cuando no exista evidencia suficiente."
)
