class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f' A pessoa se chama {self.nome} e sua idade é de {self.nome} e sua profissão é {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profisdsao:
            return 'Parabéns pela sua profissão. Espero que tenha muito sucesso!'
        else:
            return ''
    
