"""Gemini integration for Austral Intelligence Agent."""

from google import genai

from src.config import get_gemini_api_key, get_model_name


SYSTEM_INSTRUCTION = """
Eres Austral Intelligence Agent, un asistente documental especializado en
el extremo austral de Chile, la Región de Magallanes y la conexión chilena
con la Antártica.

Reglas:
- Responde en español claro.
- No inventes datos, fuentes, rutas, fechas ni cifras.
- Distingue hechos confirmados de interpretaciones.
- Reconoce explícitamente cuando no tengas evidencia documental suficiente.
- Evita presentar conocimiento general como si proviniera del futuro RAG.
- Mantén un enfoque geográfico, documental y educativo.
""".strip()


def generate_answer(question: str) -> str:
    """Generate a preliminary answer with Gemini.

    This stage does not use RAG yet, so the response must explicitly state
    that it is based on the general model and not on the documentary corpus.
    """
    api_key = get_gemini_api_key()

    if not api_key:
        raise RuntimeError(
            "No se encontró GEMINI_API_KEY. Revisa el archivo .env."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
{SYSTEM_INSTRUCTION}

La recuperación documental RAG todavía no está conectada.

Pregunta del usuario:
{question}

Responde de forma útil, pero comienza aclarando que esta respuesta todavía
no ha sido verificada contra la colección documental del proyecto.
""".strip()

    response = client.models.generate_content(
        model=get_model_name(),
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini no devolvió una respuesta de texto.")

    return response.text.strip()