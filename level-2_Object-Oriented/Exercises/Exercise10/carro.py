from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano

    def mostrar_carro(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ano {self.ano}'