from fastapi import FastAPI, HTTPException
from model import FetchAI
from dotenv import load_dotenv
from ai_agent import groq_client
from groq import AsyncGroq

load_dotenv()

app = FastAPI(
    title = "API de prueba con interacion a Groq",
    description= "Devuelve respuestas estructuradas con Pydantic",
    version="1.0.0"
)

@app.get("/")
async def home():
    """
        endpoint de bienvenida para verificar el estado de la API
    """
    return{
        "message":"Bienvenido a la API de prueba de FastAPI"
    }

@app.post("/prompt")
async def send_prompt(fetch:FetchAI):
    """
        Recibe un prompt y espera la respuesta del agente LLM
    """
    try:
        response = await groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
           messages=[
    {
        "role": "system",
        "content": f"Eres un experto técnico. Responde en máximo {fetch.answer} palabras"
    },
    {
        "role": "user",
        "content": fetch.prompt
    }
],
            temperature=0.3
        )
        return {
            "answer": response.choices[0].message.content,
            "info": "Procesando con Groq LPU"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la respuesta:{str(e)}")
