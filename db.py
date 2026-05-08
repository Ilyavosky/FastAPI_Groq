import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
if not url:
    raise ValueError("SUPABASE_URL no fue configurada en las variables de entorno")

key: str = os.environ.get("SUPABASE_KEY")
if not key:
    raise ValueError("SUPABASE_KEY no fue configurada en las variables de entorno")

supabase: Client = create_client(url, key)
