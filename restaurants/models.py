from typing import Optional
from pydantic import BaseModel


class RestOut(BaseModel):
    id: Optional[int]
    name: str
    neighborhood: str
    address: str
    cuisine_type: str


class RestIn(BaseModel):
    name: str
    address: str
