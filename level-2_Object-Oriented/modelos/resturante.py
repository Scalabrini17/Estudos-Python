from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  # O __init__() é um método "Construtor" quando chamado dentro da class assim que é colocada ela já vai gerar valores para as variaveis
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self,):  # O __str__serve para que quando a variavel que contem esses valores for chamada, venhas as informações desejadas
        return f"{self._nome} |{self._categoria}"  # self referencia da instancia que está sendo chamada no momento

    @classmethod
    def listar_restaurantes(cls):  # Podemos usar os metodos (def) do prórpio python como foito a cima e os próprios metodos nossos como dessa linha Listar_restaurante().
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}' # coloquei o media avaliação dentro do str() para colocar o ljust porque o tipo decimal não tem ljust nele, então decalrei como string antes de aparecer
            )

    @property
    def ativo(self):
        return "ativo" if self._ativo else "não ativo"
        
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return  '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) # o sum() serve para somar 
        quantidade_notas = len(self._avaliacao)   # len() serve para ver a quantidade 
        media = round(soma_notas / quantidade_notas,1) # O round() serve para escolhar quantas casas deciamis deve ter, nesse cado 1 casa decimal
        return media

