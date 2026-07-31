import os
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):                 # self é convenção, mas não precisa usar necessariamente "self"
        self._nome = nome.title()                        # o importante é que seja a mesma palavra sempre que fizer a auto-referência 
        self._categoria = categoria.upper()              # em java se usa "this". Se usar "this", funciona igual
        self._ativo = False  ###### ENTENDER ESSE underline anterior ao ativo. Deu erro sem, "property 'ativo' of 'Restaurante' object has no setter" 
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        os.system('cls')            # ----------> esse cls é do terminal, short to "clear screen" (não confundir com o cls da classe)
        print(f"{"Nome do Restaurante".ljust(27)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | {"Status"}")
        print("-_"* 50)
        for restaurante in cls.restaurantes:
            print(f"- {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "√" if self._ativo else "☐"   ###### o underline em ativo foi necessário aqui também, mas não no "def ativo(self)".
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    # ----------- essas foram as funções que foram substituidas pela "adicionar_no_cardapio"
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
    #
    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)
    #----------------------------------------------------------------------------------------

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"\nCardapio do Restaurante {self._nome}\n")          #--> não entendi por que o atributo recebe a variável em string
        for i, item in enumerate(self._cardapio, start = 1):        #|       pelo que vi, é a forma da função mesmo.
            if hasattr(item, "descricao"):            #----------------
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}"
                print(mensagem_bebida)
        print()


    

#restaurante_praca = Restaurante("Praça", "Gourmet") 
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante("Pizza Express", "Pizzaria") 


#Restaurante.listar_restaurantes()                       # vai listar todos os restaurantes, da lista criada na classe