from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

# Tabela de associação para o relacionamento many-to-many
# author_book_association = Table(
#     'author_book_association',
#     Base.metadata,
#     Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True),
#     Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
# )

class BookModel(Base):
    __tablename__ = "books"  # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)  # Chave primária
    title = Column(String, index=True)                   # Titulo do livro
    isbn = Column(String, unique=True, index=True)

    authors = relationship(
        "AuthorModel",
        secondary="author_book_association",
        back_populates="books"
    )
    
    def __repr__(self):
        return f"<BookModel(id={self.id}, title='{self.title}', isbn='{self.isbn}')>"