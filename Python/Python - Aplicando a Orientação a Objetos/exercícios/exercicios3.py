#Exercícios

#1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular=str, saldo=float):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

#2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'O titular da conta é {self._titular}; o saldo da conta é {self._saldo}'

            # vou botar as instâncias lá embaixo, porque os próximos exercicios provavelmente ainda tem a ver com esta classe
            # contas => conta1 e conta2

#3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    def ativar_conta(self):
        self._ativo = not self._ativo

            # resto do exercício lá embaixo, conta3

#4.Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

    # meu código já tinha sido escrito com as variáveis todas "(pseudo-)protegidas", com underscore no nome
    # Não entendi muito bem o que mais propunham neste exercício, ou porquê usar @property.

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    
#5.Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancaria("Paula", 4000)
print(f'O titular é {conta4.titular}')

#6.Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    lista_clientes = []
    def __init__(self,nome=str,email=str,telefone=str,cpf=str,numero_conta=int):  #não sei qual o melhor formato para as variáveis, se str ou int
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._cpf = cpf
        self._numero_conta = numero_conta
        ClienteBanco.lista_clientes.append(self)    #essa lista, apenas pra poder usar no método do exercício seguinte.

        # vou instanciar os objetvos lá embaixo novamente.

#7.Crie um método de classe para a conta ClienteBanco.
    @classmethod
    def mostrar_clientes(cls):
        for i in cls.lista_clientes:
            print(vars(i))


#ex2
conta1 = ContaBancaria("Jean", 1000)
conta2 = ContaBancaria("John", 2000)

print(conta1,'\n',conta2)

#ex3
conta3 = ContaBancaria("Daniel", 3000)
print(vars(conta3))
conta3.ativar_conta()
print(vars(conta3))

#ex6
cliente1 = ClienteBanco("Jean", "jean@gmail.com", "123", "111", 999)
cliente2 = ClienteBanco("Ana", "ana@gmail.com", "456", "222", 888)
cliente3 = ClienteBanco("Lourdes", "lourdes@gmail.com", "789", "333", 777)

ClienteBanco.mostrar_clientes()