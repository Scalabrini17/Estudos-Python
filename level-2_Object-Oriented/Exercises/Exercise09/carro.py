from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, porta):
        super().__init__(marca, modelo)
        self.porta = porta

    def __str__(self):
        return f'{super().__str__()} | Quantidade de Portas {self.porta}' #assim que se pega o str da classe pai e adiciaona o que tem na classe filha 
    
