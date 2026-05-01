from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Author(BaseModel):
    """
    Entidade Author - Versão completa com relacionamentos
    """
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    books: List['Book'] = Field(default_factory=list)

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

# Resolve forward references (necessário para relacionamentos)
from .book import Book
Author.model_rebuild()