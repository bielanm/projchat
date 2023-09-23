from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    text: str
    id: Optional[int] = None
