#exercício: fazer a Sobremesa

from modelos.cardapio.item_cardapio import ItemCardapio 
# por alguma razão, eu tenho que usar o caminho inteiro
# modelos.cardapio.item_cardapio, em vez de simplesmente "item_cardapio"
# suponho que então ele está partindo do lugar onde está o app.py

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return f"{self._nome}"
    
    def aplicar_desconto(self):             #digamos que seja 10%
        self._preco = self._preco * 0.9
        
