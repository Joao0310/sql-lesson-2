from repositories.author_repository import AuthorRepository
from entities.author import Author
from models.author_model import AuthorModel

class CreateAuthorUseCase:
    def __init__(self, author_repository: AuthorRepository): # O Use Case recebe uma instância do repositório de autores via injeção de dependência.
        self.author_repository = author_repository

    def execute(self, name: str, email: str) -> Author: # O método execute do Use Case cria um novo autor usando o repositório e retorna a entidade criada.
        author_model = AuthorModel(name=name, email=email)
        created_author = self.author_repository.add(author_model)
        return created_author
