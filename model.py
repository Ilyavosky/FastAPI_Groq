from pydantic import BaseModel

class FetchAI(BaseModel):
    prompt: str
    answer: int = 50