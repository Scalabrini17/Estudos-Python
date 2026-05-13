# Exercícios

# 1 Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
clio= Carro('Authentique', 'prata', '2012')

# 2 Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, localidade, melhor_prato):
        self.nome = nome
        self.categoria = categoria
        self.localidade = localidade
        self.melhor_prato = melhor_prato
        self.ativo = False
    
    def __str__(self):
        return '\nNome | Categoria | Localidade | Melhor_prato | Ativo \n'+f'\n{self.nome} | {self.categoria} | {self.localidade} | {self.melhor_prato} | {self.ativo}\n'

la_bella_vita = Restaurante('La Bella Vita Ristorante', 'Italiano', 'Carmiano, na provincia de Lecce', 'Polpettone de Carne')

# 3 Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor

class Cliente:
    def __init__(self, id, nome, email, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.nascimento = nascimento
    def __str__(self):
        return f'{self.id}, {self.nome}, {self.email}, {self.nascimento}'

cliente1 = Cliente('1', 'Ana Luisa', 'ana@gmail.com', '26/02/2005')
cliente2 = Cliente('2', 'Itallo Scalabrini', 'itallo@gmail.com', '19/01/2007')
cliente3 = Cliente('3', 'Izadora', 'iza@gmail.com', '26/12/2011')