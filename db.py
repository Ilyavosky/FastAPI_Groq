import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
if not url:
    raise ValueError("SUPABASE_URL no fue configurada en las variables de entorno")

api_key: str = os.environ.get("SUPABASE_KEY")
if not api_key:
    raise ValueError("SUPABASE_KEY no fue configurada en las variables de entorno")

supabase: Client = create_client(url, api_key)
