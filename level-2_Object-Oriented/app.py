from modelos.resturante import Restaurante

Restaurante_praca = Restaurante('Praça', 'Gourmet')
Restaurante_praca.receber_avaliacao('Itallo', 10)
Restaurante_praca.receber_avaliacao('Ana Luisa', 7.5)

def main():
    Restaurante.listar_restaurantes() 


if __name__ == '__main__':
    main()