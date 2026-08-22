#ex5
from exercicios4 import Livro

#ex6
    # as instâncias no arquivo exercício4 não vêm junto, apenas os prints rodam
livro6 = Livro("Os Lusíadas", "Camões", 1572)
print(livro6.disponivel)
livro6.emprestar()
print(livro6.disponivel)

#ex7
livro7 = Livro("A Tempestade", "Willian Shakespeare", 1610)
print(Livro.verificar_disponibilidade(1610))
