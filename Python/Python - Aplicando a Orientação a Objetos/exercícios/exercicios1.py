#Exercícios

#Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
from restaurante2 import Restaurante

restaurante1 = Restaurante()            #vou usar restaurante1 em vez desse nome atrapalhado que usaram. 
restaurante1._categoria = 'Italiana'

#Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
restaurante1._nome = "Praça"
nome_do_restaurante = restaurante1._nome
print(restaurante1._nome)

#Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
funcionamento = "Ativo" if restaurante1.ativo else "Inativo" 
print(f"O restaurante está {funcionamento}")

#Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante()._categoria
print(f"o valor da classe categoria é: {categoria}")

#Altere o valor do atributo nome para 'Bistrô'.
restaurante1._nome = "Bistrô"
print(restaurante1._nome)

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante2 = Restaurante()    #utilizei um número novamente, em vez de 'restaurante_pizza', que me soa uma variável confusa
restaurante2._nome = 'Pizza Place'
restaurante2._categoria = 'Fast Food'
print([restaurante2._nome, restaurante2._categoria])

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante2._categoria)

# Mude o estado da instância restaurante_pizza para ativo.
restaurante2.ativo = True
funcionamento = "Ativo" if restaurante2.ativo else "Inativo" 
print(f"O restaurante está {funcionamento}")

# Imprima no console o nome e a categoria da instância restaurante_praca.
print([restaurante1._nome, restaurante1._categoria])