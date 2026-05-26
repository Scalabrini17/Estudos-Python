from modelos.cardapio.item_cardapio import ItemCardapio
# Aqui estou fazendo com que a minha classe prato herde os atributos da classe mãe a classe ItemCardapio (assim é a herança)
class Prato(ItemCardapio): 
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # O SUPER É UM OBJETO ESPECIAL E ELE PERMITE QUE ACESSE INFORMAÇÕES DE OUTRA CLASSE
        self.descricao = descricao

    def __str__(self):
        return self._nome