from groq import AsyncGroq
import os

groq_client = AsyncGroq(
    api_key=os.environ.get("GROQ_API_KEY")
)