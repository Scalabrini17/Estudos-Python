class Restaurante:
    def __init__(self, nome, categoria): # O __init__() é um método "Construtor" quando chamado dentro da class assim que é colocada ela já vai gerar valores para as variaveis
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):      # O __str__serve para que quando a variavel que contem esses valores for chamada, venhas as informações desejadas
        return f'{self.nome} |{self.categoria}'   # self referencia da instancia que está sendo chamada no momento  

    def listar_restaurantes(): #Podemos usar os metodos (def) do prórpio python como foito a cima e os próprios metodos nossos como dessa linha Listar_restaurante().
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# Agora para criar um novo objeto precisa dos paramentros logo na frente assim como os de baixo 
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()