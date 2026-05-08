from db import supabase
from uuid import UUID

#Recibir el id de los datos de la tabla sessions
def save_message(session_id: UUID, role: str, content: str) -> dict:
    response = (
        supabase.table("messages")
        .insert({"session_id": str(session_id), "role": role, "content": content})
        .execute()
    )
    return response.data

def create_session() -> str:
    response = (
        supabase.table("sessions")
        .insert({})
        .execute()
    )
    return response.data[0]["id"]

def record(session_id: UUID) -> dict:
    response = (
        supabase.table("messages")
        .select("*")
        .eq("session_id", str(session_id))
        .order("created_at")
        .execute()
    )
    return response.data

def get_sessions() -> list:
    response = (
        supabase.table("sessions")
        .select("*")
        .order("updated_at", desc=True)
        .execute()
    )
    return response.data