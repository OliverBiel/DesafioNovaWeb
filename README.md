# Desafio Nova Web

## Bem-vindo!
Esse repositório foi criado para fazer o desafio de estágio da Nova Web.
Foi utilizado Django juntamente com um container PostgreSQL no Docker

## Instalacao

- Após clonar o repositório crie uma venv na pasta do repositório com o seguinte comando:

*Necessário ter python instalado!

```bash
python -m venv venv 
```
- Em seguida inicialize a venv da seguinte forma:

```bash
source venv/bin/activate
```
*Certifique-se que o terminal utilizado está na pasta aonde foi criada a venv.

- Tendo criado e ativado a venv basta instalar os requirements, com a terminal na pasta raiz do projeto execute o comando:
```bash
pip install -r requirements.txt
```
- É necessário ter um banco postgres para poder fazer a conexão com o django, o mesmo pode ser criado como desejar. No meu caso criei um container utilizando [Docker](https://hub.docker.com/_/postgres).
- Tendo criado o banco, basta criar um arquivo .env na pasta CVGenerator/CVGenerator/ com as seguintes variáveis:
```bash
SECRET_KEY=chave de seguranca do django (Caso voce nao possua uma, basta pesquisar no google um gerador de secret key para django)
DB_NAME=nome do DB
DB_USER=user do DB
DB_PSWD=senha do DB
DB_HOST=ip do host do DB
DB_PORT=porta do DB - Por padrao a porta do postgres e 5432, esta como default no projeto, so e necessario utilizar essa variável se voce tiver mudado a porta padrao.
```
- Depois basta rodar os comandos, com a venv ativada:
```python
python manage.py makemigrations

#apos rodar o comando acima, rode o seguinte:
python manage.py migrate
```

## Como utilizar
### Inicializando o backend

- Se tudo ocorreu corretamente basta rodar o comando com a venv ativada:
```python
python manage.py runserver
```
- Pronto, o backend da aplicação já esta rodando. Para acessar basta clicar no link que aparece no terminal.

## Contato
- [Linkedin](https://www.linkedin.com/in/gabriel-oliveira-4bb406190)