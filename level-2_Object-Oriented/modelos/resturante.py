class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  # O __init__() é um método "Construtor" quando chamado dentro da class assim que é colocada ela já vai gerar valores para as variaveis
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self,):  # O __str__serve para que quando a variavel que contem esses valores for chamada, venhas as informações desejadas
        return f"{self._nome} |{self._categoria}"  # self referencia da instancia que está sendo chamada no momento

    @classmethod
    def listar_restaurantes(cls):  # Podemos usar os metodos (def) do prórpio python como foito a cima e os próprios metodos nossos como dessa linha Listar_restaurante().
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}"
            )

    @property
    def ativo(self):
        return "ativo" if self._ativo else "não ativo"
        
    def alternar_estado(self):
        self._ativo = not self._ativo


