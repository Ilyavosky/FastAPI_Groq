from pydantic import BaseModel, Field

class FetchAI(BaseModel):
    prompt: str = Field(min_length=1, max_length=1000)
    max_words: int = Field(default=50, ge=10, le=500)