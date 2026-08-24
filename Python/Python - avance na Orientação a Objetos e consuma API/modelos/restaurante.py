from modelos.avaliacao2 import Avaliacao        # o professor usou modelos.avaliacao2, mas eu entendo que esse arquivo já está na pasta modelos.  
#                                               # única explicação é que o 'ponto de partida' é o app2.py, e não este arquivo restaurante2.py
class Restaurante:                              # alternativamente, descobri que dá pra usar "from .avaliacao2", já que estão na mesma pasta.
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod        # aqui não faz diferença, porque tenho apenas a classe Restaurante. Mas cls é útil quando há herança
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes()).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):     # demorei pra compreender esse decorador @property. Agora caiu a ficha de porquê ativo e _ativo
        return '✓' if self._ativo else '✘' 

    def alternar_estado(self):
        self._ativo = not self._ativo


        # Métodos relacionados à avaliação
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    #@property           # não compreendi exatamente por que usar esse método como property. Parece questão de gosto.
    #                    # parece que a intenção tem a ver com a utilização sem parênteses no for em "listar_restaurantes"
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    

#restaurante_praca = Restaurante()
# restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Gourmet'


#restaurante_praca = Restaurante('prAça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('PiZza exPress', 'Italiana')

#restaurantes = [restaurante_praca, restaurante_pizza]

    # tudo que eu boto aqui, mesmo que não faça parte da classe, roda junto quando importo o código em outro arquivo
#print(dir(restaurante_praca))       #mostra todos os atributos, métodos e variáveis da classe
#print(vars(restaurante_praca))      #mostra um dicionário com os atributos que eu defini (nome e categoria; ativo eu não atribui valor então não mostra.)
#print(restaurante_praca.ativo)

#Restaurante.listar_restaurantes()



