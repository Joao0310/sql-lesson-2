from app.entities.author import Author
from app.entities.book import Book

def test_entities():
    # Testando validações
    print("=== Testando Entidades ===")

    # Autor válido
    author = Author(
        name="Clarice Lispector",
        email="clarice@email.com"
    )
    print(f"✅ Autor criado: {author}")

    # Livro válido
    book = Book(
        title="A Hora da Estrela",
        isbn="978-8520925829"
    )
    print(f"✅ Livro criado: {book}")

    # Testando validações que devem falhar
    try:
        # Nome vazio
        invalid_author = Author(name="", email="test@email.com")
    except ValueError as e:
        print(f"❌ Validação funcionou - Nome vazio: {e}")

    try:
        # Email inválido
        invalid_author = Author(name="Test", email="email-inválido")
    except ValueError as e:
        print(f"❌ Validação funcionou - Email inválido: {e}")

    try:
        # ISBN muito curto
        invalid_book = Book(title="Test", isbn="123")
    except ValueError as e:
        print(f"❌ Validação funcionou - ISBN inválido: {e}")

if __name__ == "__main__":
    test_entities()