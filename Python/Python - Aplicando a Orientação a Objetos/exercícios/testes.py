class Restaurante:
    lista_de_restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        Restaurante.lista_de_restaurantes.append(self)

    def listar_restaurantes():
        for i in Restaurante.lista_de_restaurantes:
            print(i.nome, i.categoria)

rest1 = Restaurante('A', '1')
rest2 = Restaurante('B', '2')
rest3 = Restaurante('C', '3')

Restaurante.listar_restaurantes()