#Exercícios

#1.Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def __str__(self):
        return str(vars(self))      #gambiarra com o str pra forçar o retorno a ser string. Apenas pra poder printar e ver o resultado

carro1 = Carro("siena", "azul", 2001)       # olhando a resolução proposta, fizeram o seguinte:
print(carro1)                               # meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)
#                                           # achei elegante e legível, porque deixa claro qual variável é qual.

#2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome=str, categoria=str, ativo=bool, lotacao=int, localizacao=str):
        self.nome = nome
        self.categoria = categoria      # pensei que informar o tipo de variável na classe faria o programa dar problema se informasse outro tipo
        self.ativo = ativo              # mas o python aceita normalmente qualquer variável atribuída.
        self.lotacao = lotacao
        self.localizacao = localizacao

    def __str__(self):
        return str(vars(self))

restaurante1 = Restaurante("Rock n Grill", "prato feito", True, 300.0, "Shopping Estação")
print(restaurante1)

#3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante2:
    def __init__(self, nome='', categoria='', ativo=False):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = ativo    

    def __str__(self):
        return str(vars(self))

restaurante2 = Restaurante2("Mc Donalds", "Fast Food")      #basta omitir a variável ativo, ela já tem um valor default.
print(restaurante2)

#4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# esses métodos __str__ já incluí em todas, então não vou fazer uma nova classe apenas pra isso. Vou usar no próximo exercício também

#5.Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, contato, documento):
        self.nome = nome
        self.idade = idade
        self.contato = contato
        self.documento = documento

    def __str__(self):
        return str(vars(self))

cliente1 = Cliente("Jean", 40, "99887766", "11223344")
cliente2 = Cliente("Fulano", 21, "91231231", "345345345")
cliente3 = Cliente("Ciclano", 33, "98877665", "192837456")