from flask_sqlalchemy import SQLAlchemy # primerio passo para utilizar o banco no flask: da biblioteca flask_sqlalchemy importa o SQLAlchemy, biblioteca
# que facilita a integração do Flask com o SQLAlchemy

from flask_login import UserMixin 


db = SQLAlchemy() # segundo passo para utilizar o banco no flask : cria o objeto db que instancia o SQLAlchemy



#terceiro passo para utilizar o banco no flask: cria as tabelas no banco de dados

# tabelinha de usuarios - herda de db.Model a função column e tipos de dados

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome =db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# tabelinha de produtos - herda de db.Model a função column e tipos de dados

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    nome =db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)