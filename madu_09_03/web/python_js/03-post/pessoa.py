class Pessoa:
    # construtor com valor padrão nos parâmetros
    def __init__(self, nome="", email="", telefone="", dt_nasc=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento= dt_nasc

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}, {self.data_nascimento}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone,
            "nasc" :  self.data_nascimento
        }