# Requirements

## Requisitos funcionales del MVP

- Permitir al usuario escribir una consulta en una interfaz web.
- Recuperar fragmentos relevantes desde una colección documental controlada.
- Generar una respuesta basada en el contexto recuperado.
- Mostrar las fuentes utilizadas.
- Indicar claramente cuando la evidencia sea insuficiente.
- Mantener separados los documentos originales y los datos procesados.

## Requisitos no funcionales

- URL pública para evaluación.
- Configuración mediante variables de entorno.
- Ninguna clave API almacenada en GitHub.
- Código modular y documentado.
- Tiempo de respuesta razonable para una demostración.
- Registro básico de errores sin exponer secretos.

## Fuera del alcance inicial

- Rastreo autónomo masivo de internet.
- Respuestas médicas, legales o financieras.
- Procesamiento automático de una biblioteca documental extensa.
- Sistema multiagente complejo antes de validar el MVP.

## Criterios de aceptación

- La aplicación se ejecuta localmente con `streamlit run app.py`.
- Existe una versión desplegada mediante URL pública.
- Una consulta de demostración devuelve respuesta y fuentes.
- Una consulta sin respaldo genera una advertencia en vez de inventar información.
