from modelos.resturante import Restaurante

Restaurante_praca = Restaurante('Praça', 'Gourmet')
Restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
Restaurannte_japones = Restaurante('Japa', 'Japonesa')

Restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes() 


if __name__ == '__main__':
    main()