from app.database.database import SessionLocal, Base, engine
from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.repositories.author_repository import AuthorRepository
from app.repositories.book_repository import BookRepository

def main():
    # Criar uma sessão
    session = SessionLocal()

    try:
        # Instanciar repositórios
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        author_book_association = Base.metadata.tables.get("author_book_association")

        # Apagar dados existentes para o exemplo
        session.query(AuthorModel).delete()
        session.query(BookModel).delete()
        session.query(author_book_association).delete()

        # Criar um autor
        author = AuthorModel(
            name="Machado de Assis",
            email="machado@email.com"
        )
        author = author_repo.add(author)
        print(f"Autor criado: {author}")

        # Criar um livro
        book = BookModel(
            title="Dom Casmurro",
            isbn="978-8525406958"
        )
        book = book_repo.add(book)
        print(f"Livro criado: {book}")

        # Associar autor ao livro
        book.authors.append(author)
        session.commit()

        # Buscar autor por email
        found_author = author_repo.get_by_email("machado@email.com")
        print(f"Autor encontrado: {found_author}")
        print(f"Livros do autor: {[book.title for book in found_author.books]}")

        # Buscar livro por título
        found_books = book_repo.get_by_title("Dom")
        print(f"Livros encontrados: {[book.title for book in found_books]}")

    finally:
        session.close()

if __name__ == "__main__":
    main()