"""Gemini integration for Austral Intelligence Agent."""

from google import genai

from src.config import get_gemini_api_key, get_model_name


SYSTEM_INSTRUCTION = """
Eres Austral Intelligence Agent, un asistente documental especializado en
el extremo austral de Chile, la Región de Magallanes y la conexión chilena
con la Antártica.

Reglas:
- Responde en español claro.
- Comienza directamente con la respuesta documental.
- No uses saludos, fórmulas de cortesía ni presentaciones como "Estimado/a",
  "A continuación", "He procesado los documentos" o "Como asistente".
- No inventes datos, fuentes, rutas, fechas ni cifras.
- Distingue hechos confirmados de interpretaciones.
- Reconoce explícitamente cuando no tengas evidencia documental suficiente.
- Evita presentar conocimiento general como si proviniera del RAG.
- Mantén un enfoque geográfico, documental y educativo.
""".strip()


def generate_answer(
    question: str,
    context: str = "",
) -> str:
    """Generate an answer with optional documentary context."""
    api_key = get_gemini_api_key()

    if not api_key:
        raise RuntimeError(
            "No se encontró GEMINI_API_KEY. Revisa el archivo .env."
        )

    client = genai.Client(api_key=api_key)

    if context.strip():
        evidence_block = f"""
Contexto documental recuperado:
{context}

Reglas adicionales:
- Responde utilizando solamente el contexto documental disponible.
- No agregues datos externos como si estuvieran confirmados.
- Si el contexto no contiene la respuesta, indícalo claramente.
- Menciona las fuentes proporcionadas al final de la respuesta.
- Inicia con la conclusión o información principal, sin saludo previo.
""".strip()
    else:
        evidence_block = """
No se recuperó contexto documental relevante.

Indica directamente que no existe evidencia suficiente en la colección local
para responder, sin usar saludos ni fórmulas de cortesía.
""".strip()

    prompt = f"""
{SYSTEM_INSTRUCTION}

{evidence_block}

Pregunta del usuario:
{question}
""".strip()

    response = client.models.generate_content(
        model=get_model_name(),
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini no devolvió una respuesta de texto.")

    return response.text.strip()
