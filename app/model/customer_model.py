"""
ORM and schema models
"""
from pydantic import BaseModel, Field
from datetime import datetime

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    created_at: datetime = Field(default_factory=datetime.now)