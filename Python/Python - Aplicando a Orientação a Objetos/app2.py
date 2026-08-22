from modelos.restaurante2 import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Jean', 9)
restaurante_praca.receber_avaliacao('Ana', 2)
restaurante_praca.receber_avaliacao('Bento', 7.5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()