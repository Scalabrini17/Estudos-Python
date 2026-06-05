from abc import abstractmethod

class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    @abstractmethod
    def ligar(self):
        pass
