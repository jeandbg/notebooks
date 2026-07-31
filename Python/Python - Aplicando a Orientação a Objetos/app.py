from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca    = Restaurante("Praça da Pizza", "Gourmet")
#restaurante_mexicano = Restaurante("Mexican Food","comida mexicana")
#restaurante_japones =  Restaurante("Japo","comida japonesa")

#restaurante_mexicano.alternar_estado()

#restaurante_praca.receber_avaliacao("Gui", 10)
#restaurante_praca.receber_avaliacao("Lais", 8)
#restaurante_praca.receber_avaliacao("Emy", 5)

bebida_suco = Bebida("Suco de Melancia", 5.0, "grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Paozinho na manteiga", 2.0, "O melhor pão da cidade")
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

# EXERCÍCIO -- INCLUIR SOBREMESA
# sobremesa_pave = Sobremesa("Pavê", 5.0, "Doce", "grande", "Pavê ou pra Comer?")
# sobremesa_pave.aplicar_desconto()
# restaurante_praca.adicionar_no_cardapio(sobremesa_pave)




def main():
    #Restaurante.listar_restaurantes()
    # print(bebida_suco)
    # print(prato_paozinho)
    restaurante_praca.exibir_cardapio
    #print(sobremesa_pave)

if __name__ == "__main__":
    main()