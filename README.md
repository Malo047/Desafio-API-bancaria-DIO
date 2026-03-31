API REST desenvolvida com FastAPI para simular operações bancárias, incluindo autenticação com JWT e rotas protegidas.

Tecnologias utilizadas:
Python
FastAPI
Uvicorn
JWT (Autenticação)

Funcionalidades
Autenticação
Criação de contas
Depositos, saques e histórico de transações
Rotas protegidas
Estrutura preparada para banco de dados

COMO EXECUTAR O PROJETO

Clone o repositório com git clone
Ative o ambiente virtual com: src\venv\Scripts\activate
Instale as dependências: pip install fastapi uvicorn PyJWT
Execute a aplicação: uvicorn src.main:app --reload

AUTENTICAÇÃO

Endpoint de login
POST /login/
Corpo da requisição:
{
  "username": "marlon",
  "password": "123"
}
Resposta
{
  "access_token": "seu_token_aqui",
  "token_type": "bearer"
}
COMO USAR O TOKEN
Copiar o access_token
Vá até o ThunderClient, Postman, Insomnia
Na Aba Auth, selecione Bearer Token e cole o token

O projeto usa um fake_DB com a estrutra preparada para receber um banco de dados

Melhorias futuras
Integração com banco de dados 
Criptografia com bcrypt
sistema de autorização com roles
refresh token

Desennvolvido por Marlon Hoffmann
