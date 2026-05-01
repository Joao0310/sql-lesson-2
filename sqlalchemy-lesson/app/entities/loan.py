from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from .book import Book

class Loan(BaseModel):
    """
    Entidade Loan - Versão completa com relacionamentos
    """
    id: Optional[int] = None
    book_id: int
    user_name: str = Field(..., min_length=3, max_length=100)
    loan_date: date
    return_date: Optional[date] = None
    returned: bool = False

    book: Optional[Book] = None

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Loan: {self.user_name} -> Book {self.book_id}"