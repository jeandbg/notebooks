import os

restaurantes = [
    {"nome":"Pizza Place",       "categoria":"Pizzaria",    "ativo":False},
    {"nome":"Sushi do Jão",      "categoria":"Sushi",       "ativo":True},
    {"nome":"Cantina da Comida", "categoria":"Italiana",    "ativo":True},
    ]

def exibir_nome_do_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizar App")

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()

def opcao_invalida():
    print("Opção Invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do Restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
 
    print(f"{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status" )
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"* {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
                # A sintaxe dessa linha acima é meio confusa inicialmente. É o que o professor chamou de "ternário". 
                # É uma forma concisa de criar um if-else de apenas uma condição.
                # A estrutura é "VALOR VERDADEIRO if CONDIÇÃO VERDADEIRA else VALOR FALSO"
            print(mensagem)
        if not restaurante_encontrado:
            print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

        #alternativamente, e talvez de forma mais elegante, o menu poderia ser enunciado assim:
        # match opcao_escolhida:
        #case 1:
        #    print('Adicionar restaurante')
        #case 2:
        #    print('Listar restaurantes')
        #case 3:
        #    print('Ativar restaurante')
        #case 4:
        #    print('Finalizar app')
        #case _:
        #    print('Opção inválida!')
    except:
        opcao_invalida()



def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


#print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n')
#nunca tinha visto essa sintaxe de usar separador "sep = 'x' "