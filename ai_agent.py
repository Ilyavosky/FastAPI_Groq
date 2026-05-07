from groq import AsyncGroq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY no está configurada en el entorno")

groq_client = AsyncGroq(api_key=api_key)