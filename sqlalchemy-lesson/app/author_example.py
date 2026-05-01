from app.entities.author import Author

# Criando um autor válido
author = Author(
    name="Machado de Assis",
    email="machado@email.com"
)

print("============= Autor Válido =============")
print(author)  # Author: Machado de Assis (machado@email.com)
print()
print(author.model_dump())  # {'id': None, 'name': 'Machado de Assis', 'email': 'machado@email.com'}
print()
# Tentando criar autor inválido
try:
    print("============= Tentando criar Autor Inválido =============")
    invalid_author = Author(
        name="",  # ← Nome vazio! Vai dar erro
        email="email-inválido"  # ← Email inválido! Vai dar erro
    )
except ValueError as e:
    print(f"Erro de validação: {e}")