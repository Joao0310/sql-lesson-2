# Criacao de Autor
## Descricao
Cria um novo autor com os dados fornecidos no corpo da requisição.
## Parametros
- **name** (str): Nome completo do autor. Exemplo: "João"
- **email** (str): Email válido do autor. Exemplo: "joao@example.com"

## Resposta
- **200 OK**: Retorna o autor criado.
- **400 Bad Request**: Retorna um erro se os dados fornecidos forem inválidos.
