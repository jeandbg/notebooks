#Exercícios

#1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    lista_de_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_de_livros.append(self)

        # instâncias criadas lá embaixo.

#2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'Título: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'

        #instâncias e prints lá embaixo


#3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self._disponivel = not self._disponivel
    #              # apesar do texto do exercício, acredito que eles queiram que esta função permita alterar False e True

    @property               # resolvi fazer uma property em vez de simplesmente printar as variáveis
    def disponivel(self):
        return f"O livro '{self._titulo}' está disponível" if self._disponivel else f"O livro '{self._titulo}' não está disponível"

            # instâncias e prints lá embaixo


#4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    
    @staticmethod                # métodos estáticos não estavam no curso, mas o ChatGPT me explicou
    def verificar_disponibilidade(ano):
        livros_disponiveis = []

        for livro in Livro.lista_de_livros:
            if (livro._ano_publicacao == ano and livro._disponivel):
                livros_disponiveis.append(livro)

        return livros_disponiveis

    def __repr__(self):
        return f'{self._titulo} | {self._ano_publicacao} | {self._disponivel}'


#5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
    #feito, verificar no arquivo biblioteca

#6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

#7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

#8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.


#ex1
livro1 = Livro('A Metamorfose', 'Franz Kafka', 1915)
livro2 = Livro('Os Miseráveis', 'Victor Hugo', 1862)

#ex2
livro3 = Livro('Os Três Mosqueteiros', 'Alexandre Dumas', 1844)
livro4 = Livro('O Grande Gatsby', 'F Scott Fitzgerald', 1925)

print(livro3)
print(livro4)

#ex3
livro5 = Livro('Paraíso Perdido', 'John Milton', 1667)
print(livro5.disponivel)
livro5.emprestar()
print(livro5.disponivel)

livros1915 = Livro.verificar_disponibilidade(1915)
print(livros1915)