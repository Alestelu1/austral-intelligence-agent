# Austral Intelligence Agent

Agente documental desarrollado para el Challenge final de Alura ONE / AI for Tech.

Permite consultar una colección controlada de fuentes sobre el extremo austral de Chile, Magallanes, Puerto Williams y la conexión chilena con la Antártica.

## Demo pública

https://austral-intelligence-agent.streamlit.app

## Problema

La información sobre conectividad austral, logística antártica, patrimonio y territorio se encuentra dispersa entre documentos institucionales, guías turísticas y sitios oficiales.

Esto dificulta encontrar respuestas rápidas, verificables y acompañadas de sus fuentes.

## Solución

Austral Intelligence Agent combina:

- una interfaz web en Streamlit;
- Gemini como modelo generativo;
- recuperación local de documentos;
- lectura de Markdown y PDF;
- división de documentos en fragmentos;
- ranking por palabras y frases;
- respuestas restringidas al contexto recuperado;
- citas con nombre de fuente y número de página;
- reconocimiento explícito cuando no existe evidencia suficiente.

## Funcionalidades del MVP

- Consultas en lenguaje natural.
- Ingesta de archivos PDF por página.
- Ingesta de fuentes web convertidas a Markdown.
- Recuperación de fragmentos relevantes.
- Respuestas documentales generadas con Gemini.
- Visualización de fuentes recuperadas.
- Eliminación de citas duplicadas.
- Despliegue público en Streamlit Community Cloud.
- Gestión segura de la API key mediante variables de entorno.

## Ejemplos de consultas

```text
¿Cómo se puede viajar desde Punta Arenas a Puerto Williams?

¿Por qué Punta Arenas es una puerta de entrada a la Antártica?

¿Cómo se conecta Chile por vía aérea con la Antártica?
```

## Fuentes incorporadas

El corpus inicial incluye:

- Manual de Destinos Turísticos Patagonia Austral y Antártica Chilena.
- Guía turística de Puerto Williams e isla Navarino.
- Instituto Antártico Chileno.
- Ministerio de Relaciones Exteriores de Chile.
- DAP Airlines.

Las fuentes operativas pueden cambiar. Los horarios, frecuencias, contactos y servicios deben verificarse en sus sitios oficiales.

## Arquitectura

```text
Usuario
  ↓
Streamlit
  ↓
Carga de documentos Markdown y PDF
  ↓
Fragmentación y ranking
  ↓
Contexto documental recuperado
  ↓
Gemini
  ↓
Respuesta con fuentes
```

## Estructura principal

```text
austral-intelligence-agent/
├── app.py
├── requirements.txt
├── data/
│   ├── documents/
│   └── raw/
│       └── pdf/
└── src/
    ├── config.py
    ├── rag/
    │   ├── document_loader.py
    │   └── retriever.py
    └── services/
        └── gemini_service.py
```

## Tecnologías

- Python
- Streamlit
- Google Gemini API
- pypdf
- python-dotenv
- GitHub
- Streamlit Community Cloud

## Ejecución local

Clona el repositorio:

```bash
git clone https://github.com/Alestelu1/austral-intelligence-agent.git
cd austral-intelligence-agent
```

Crea el entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Crea `.env` usando `.env.example` como referencia:

```env
GEMINI_API_KEY=tu_clave
MODEL_NAME=gemini-3.5-flash
```

Ejecuta la aplicación:

```bash
python -m streamlit run app.py
```

## Seguridad

- `.env` no debe subirse a GitHub.
- La API key se configura mediante Secrets en Streamlit Community Cloud.
- El repositorio solo contiene `.env.example`.

## Limitaciones actuales

- El recuperador utiliza ranking léxico y refuerzo de frases, no embeddings.
- El corpus todavía es reducido.
- Algunos documentos contienen información operativa histórica.
- Las páginas visuales o escaneadas pueden requerir OCR.
- La validación humana sigue siendo necesaria al incorporar nuevas fuentes.

## Próximas mejoras

- Embeddings y búsqueda semántica.
- Metadatos estructurados por fuente.
- Advertencias automáticas de vigencia.
- Ingestión controlada de sitios web.
- Evaluación del recuperador.
- Filtros por territorio, tema y tipo de fuente.
- Panel de administración del corpus.

## Autor

Alexis Stelu

Proyecto relacionado con Austral Beacon Media y su futura base documental sobre el extremo austral de Chile.

