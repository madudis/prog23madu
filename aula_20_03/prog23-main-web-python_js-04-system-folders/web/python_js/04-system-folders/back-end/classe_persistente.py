# exemplo mínimo
# derivado de: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

# importações
# ***********
# pip3 install flask
# pip3 install flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
# *************
# vínculo com o Flask
app = Flask(__name__) 
# sqlalchemy usando sqlite
# obter o caminho do arquivo atual
caminho = os.path.dirname(os.path.abspath(__file__))
# concatenar o caminho com o nome do arquivo de banco de dados
arquivobd = os.path.join(caminho, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + "madu"
# vínculo com o SQLAlchemy
db = SQLAlchemy(app) 

# criando contexto para a aplicação :-/
with app.app_context():

    # classe
    # ******
    class Pessoa(db.Model):
        # atributos da pessoa
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.Text)
        email = db.Column(db.Text)
        telefone = db.Column(db.Text)

        # método para expressar a pessoa em forma de texto
        def __str__(self):
            return f'(id={self.id}) {self.nome}, '+\
                f'{self.email}, {self.telefone}'

    # teste da classe
    # ***************

    # criar tabelas
    # se alterar a classe, precisa apagar o arquivo para
    # que as tabelas sejam criadas novamente!
    db.create_all()

    # teste da classe Pessoa: duas instâncias
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
        telefone = "47 98822 2531")        

    # persistir as duas pessoas
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    # exibir uma pessoa
    print(p2)
    print(p1)