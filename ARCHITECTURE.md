# Architecture

## Arquitectura inicial

```text
Usuario
  ↓
Streamlit UI
  ↓
Servicio de consulta
  ├── Recuperación documental
  ├── Construcción de contexto
  └── Generación con LLM
  ↓
Respuesta con fuentes
```

## Componentes previstos

- `app.py`: interfaz y punto de entrada.
- `src/services/`: integración con modelos y servicios externos.
- `src/rag/`: carga, división, recuperación y referencias.
- `src/agents/`: lógica del agente cuando el flujo básico esté validado.
- `src/utils/`: configuración, validación y utilidades.
- `data/raw/`: documentos originales de demostración.
- `data/processed/`: contenido transformado para recuperación.
- `prompts/`: instrucciones versionadas.
- `tests/`: pruebas unitarias y de comportamiento.

## Decisiones iniciales

- Comenzar con un flujo RAG simple antes de incorporar múltiples agentes.
- Usar Streamlit para acelerar la validación y obtener una URL pública.
- Mantener la capa del modelo desacoplada para poder cambiar de proveedor.
- Conservar referencias de procedencia en cada fragmento documental.
