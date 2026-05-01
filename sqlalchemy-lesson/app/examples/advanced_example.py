from app.database.database import SessionLocal, Base, init_db
from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.models.loan_model import LoanModel
from app.repositories.author_repository import AuthorRepository
from app.repositories.book_repository import BookRepository
from app.repositories.loan_repository import LoanRepository
from app.entities.author import Author
from app.entities.book import Book
from app.entities.loan import Loan
from datetime import date

def main():
    # Criar uma sessão
    init_db()
    session = SessionLocal()

    try:
        # Instanciar repositórios
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        author_book_association = Base.metadata.tables.get("author_book_association")

        # Apagar dados existentes para o exemplo
        session.query(author_book_association).delete()
        session.query(AuthorModel).delete()
        session.query(BookModel).delete()
        session.commit()

        
        author1_entity = Author(name="Machado de Assis", email="machado@email.com")
        author2_entity = Author(name="Clarice Lispector", email="clarice@email.com")

        author1 = author_repo.add(AuthorModel(name=author1_entity.name, email=author1_entity.email))
        author2 = author_repo.add(AuthorModel(name=author2_entity.name, email=author2_entity.email))

        book1_entity = Book(title="Dom Casmurro", isbn="1234567890")
        book2_entity = Book(title="A Hora da Estrela", isbn="1234567891")
        book3_entity = Book(title="Memórias Póstumas", isbn="1234567892")

        book1 = book_repo.add(BookModel(title=book1_entity.title, isbn=book1_entity.isbn))
        book2 = book_repo.add(BookModel(title=book2_entity.title, isbn=book2_entity.isbn))
        book3 = book_repo.add(BookModel(title=book3_entity.title, isbn=book3_entity.isbn))

        book1.authors.append(author1)
        book2.authors.append(author2)

        book3.authors.append(author1)
        book3.authors.append(author2)

        session.commit()

        print("Livros com autores:")
        books = book_repo.get_books_with_authors()
        for b in books:
            print(f"{b.title} -> {[a.name for a in b.authors]}")

        print("Buscar por título parcial:")
        found = book_repo.get_by_title("Dom")
        print([b.title for b in found])

        print("Autores com livros:")
        authors_with_books = author_repo.get_authors_with_books()
        print([a.name for a in authors_with_books])

        print("Livros da Clarice:")
        clarice = author_repo.get_by_email("clarice@email.com")
        print([b.title for b in clarice.books])


        print("Atualizando livro...")
        updated_entity = Book(title="Dom Casmurro (Atualizado)", isbn=book1.isbn)
        book1.title = updated_entity.title

        updated_book = book_repo.update(book1)
        print("Novo título:", updated_book.title)


        print("Deletando livro...")
        book_to_delete = book_repo.get_by_isbn("1234567891")
        if book_to_delete:
            book_repo.delete(book_to_delete.id)
            print(f"{book_to_delete.title} removido")


        loan_repo = LoanRepository(session)

        loan_entity = Loan(
            book_id=book1.id,
            user_name="João",
            loan_date=date.today()
        )

        loan_model = LoanModel(
            book_id=loan_entity.book_id,
            user_name=loan_entity.user_name,
            loan_date=loan_entity.loan_date,
            return_date=loan_entity.return_date,
            returned=loan_entity.returned
        )

        loan = loan_repo.add(loan_model)
        print("Empréstimo criado:", loan)

        print("Empréstimos em aberto:")
        open_loans = loan_repo.get_open_loans()
        for l in open_loans:
            print(l)

        print("Devolvendo livro...")
        loan_repo.return_book(loan.id)

        print("Após devolução:")
        for l in loan_repo.get_all():
            print(l, "-> returned:", l.returned)
    finally:
        session.close()


if __name__ == "__main__":
    main()