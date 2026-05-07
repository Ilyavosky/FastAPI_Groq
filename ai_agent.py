from groq import AsyncGroq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY no está configurada en el entorno")

groq_client = AsyncGroq(api_key=api_key)

async def ask(prompt : str, max_words: int ) -> str:
    response = await groq_client.chat.completions.create(
        model= os.environ.get("GROQ_MODEL"),
        messages= [
            {
                "role": "system",
                "content": f"Eres un experto técnico. Responde en máximo {max_words} palabras"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature= 1
    )
    return response.choices[0].message.content 
    
