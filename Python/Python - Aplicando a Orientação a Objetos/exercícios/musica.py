#exercício 1.5 - Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo

class Musica:
    nome = str
    artista = str
    duracao = int

musica1 = Musica()
print([musica1.nome, musica1.artista, musica1.duracao])

musica1.nome = 'Angels Cry'
musica1.artista = 'Angra'
musica1.duracao = 300

print([musica1.nome, musica1.artista, musica1.duracao])


#exercício 2.6 - Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.
class Musica2:
    def __init__(self, nome='', artista='', duracao=0): #colocar essas definições 'default' permitem declarar uma variável sem informar os construtores
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica2 = Musica2()
print(vars(musica2))

musica3 = Musica2('Anima Mundi', 'Dionysus', '360')
print(musica3)
print(vars(musica3))