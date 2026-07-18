# Austral Intelligence Agent

Proyecto para el Challenge final de Alura ONE / AI for Tech.

Agente de IA orientado a investigar, organizar y recuperar conocimiento confiable sobre el extremo austral de Chile, Patagonia, Magallanes y la conexión antártica.

## Estado

En planificación y desarrollo inicial.

## MVP

- Interfaz web en Streamlit.
- Consultas sobre una base documental acotada.
- Respuestas con fuentes y advertencias cuando falte evidencia.
- Arquitectura preparada para incorporar RAG.

## Tecnologías iniciales

- Python
- Streamlit
- Gemini API
- GitHub
- Streamlit Community Cloud

## Ejecución local

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Nunca publiques claves API. Copia `.env.example` como `.env` y completa las variables solo en tu equipo o plataforma de despliegue.
