#3.6 Mão na massa: refatorando uma função
# A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. 
# Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como título, autor e número de páginas:

class Livro: 
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self,nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'seu nome é {self.nome}, tem {self.idade} anos e sua profissão é {self.profissao}'

    def aniversario(self):
        print(f'Meus parabéns. Você tinha {self.idade}')
        self.idade = self.idade + 1
        print(f'mas hoje é seu aniversário e você está fazendo {self.idade}')

    #não tinha entendido que 'propriedade' se referia ao decorator '@property'.
    #de igual forma, não vejo por quê ou como usar property numa mensagem desse tipo
    @property
    def saudacao(self):
        print(f"Olá senhor {self.profissao}")

pessoa1 = Pessoa('Jean',35,'bancário')
print(pessoa1)
pessoa1.aniversario()
pessoa1.saudacao

    