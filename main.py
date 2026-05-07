from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import FetchAI
from ai_agent import ask

app = FastAPI(
    title="API de prueba con interacción a Groq",
    description="Devuelve respuestas estructuradas con Pydantic",
    version="1.0.5"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    #Endpoint de bienvenida para verificar el estado de la API
    return {"message": "Bienvenido a la API de prueba de FastAPI"}

@app.post("/prompt")
async def send_prompt(fetch: FetchAI):
    #Recibe un prompt y espera la respuesta del agente LLM
    try:
        answer = await ask(fetch.prompt, fetch.max_words)
        return {
            "answer": answer,
            "info": "Procesando con Groq LPU"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))