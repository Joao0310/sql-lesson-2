from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class LoanModel(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_name = Column(String, nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    returned = Column(Boolean, default=False)

    # relacionamento com Book
    book = relationship("BookModel")

    def __repr__(self):
        return f"<LoanModel(id={self.id}, user='{self.user_name}', book_id={self.book_id}, returned={self.returned})>"