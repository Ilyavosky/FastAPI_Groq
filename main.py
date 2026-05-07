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
    answer = await groq_client
except:
    pass

