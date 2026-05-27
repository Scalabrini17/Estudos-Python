class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Estado: {self._ligado}'
    
    @property
    def ligado(self):
        return 'Desligado' if self._ligado else 'Ligado'
