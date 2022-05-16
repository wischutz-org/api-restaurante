from typing import Optional
from pydantic import BaseModel


class Restaurant(BaseModel):
    id: Optional[int]
    name: str
    neighborhood: str
    address: str
    cuisine_type: str
