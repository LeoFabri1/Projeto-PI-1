from Estoque.InterfaceEstoque import Cadastro, Altero, Deleto, Filtro
def Home():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |        |        |        |         |        |     |")
    print("|HOME|        |CARDAPIO|        |SOBRE NÓS|        |LOGIN|")
    print("|    |        |        |        |         |        |     |")
    print("")
    print("EXPLORE SEU #MOMENTO COREANO")
    print("")
    print("        Principais             Porçoes(Acompanhamentos)")
    print("**********************************************************")

#Imprime A Pagina de Estoque
def CardapioAdm():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("AJUSTE DE CARDAPIO")
    print("")
    print("               |    1-Adicionar Item    |")
    print("               |     2-Alterar item     |")
    print("               |     3-Excluir Item     |")
    print("               |        4-Filtrar       |")
    print("               |    5-Ajuste Cardapio   |")
    print("               |       6-Deslogar       |")
    print("**********************************************************")
    while True:
        opcao = input("Digite a opçao desejada")

        if opcao == "1" or opcao == "Adicionar Item":
            Cadastro()
        elif opcao == "2" or opcao == "Alterar Item":
            Altero()
        elif opcao == "3" or opcao == "Excluir Item":
            Deleto()
        elif opcao == "4" or opcao == "Filtrar":
            Filtro()
        elif opcao == "5" or opcao == "Ajuste Cardapio":
            CardapioAdm()
        elif opcao == "6" or opcao == "Deslogar":
            Home()

def CardapioCliente():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARDAPIO")
    print("")
    #Codigo que adiciona Novos itens ao cardapio, (trazer de Cadastrar())
    print("*KIMCHI*")
    print("Kimchi é tradicionalmente feito com acelga, gengibre e pimenta\nEsse é um prato que pode ser acompanhado em todas as refeições")
    print("*BIBIMBAP*")
    print("Bibimbap consiste basicamente em arroz branco, vegetais e carne misturados\nPreparados em tigela de pedra vulcânica")
    print("**********************************************************")

def Comida():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("KIMCHI")
    print("'FOTO'          Prato feito com acelga, gengibre e pimenta")
    print("Escolha abaixo a quantidade que deseja pedir:")
    print("'Caixa de escolha'                                 R$Valor")
    print("                                     Adicionar ao carrinho")
    print("**********************************************************")

def Carrinho():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARRINHO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARRINHO")
    print("")
    print("Este são os itens que estao em seu carrinho:")
    print("Kimchi, 1 unidade  -  R$Valor")
    print("")
    print("                                          Subtotal:R$Valor")
    print("                                             Frete:R$Valor")
    print("                                             Total:R$Valor")
    print("                                          Finalizar pedido")
    print("**********************************************************")

def Pagamento():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("Endereço de entrega:                    Forma De Pagamento")
    print("CEP:                                                   Pix")
    print("Nome completo:                       Cartao Credito/Debito")
    print("Numero de Celular:                                  Boleto")
    print("                                       Finalizar Pagamento")
    print("**********************************************************")

def Login():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |")
    print("|HOME|")
    print("|    |")
    print("")
    print("ÁREA DE LOGIN")
    print("              Usuario:")
    print("                Senha:")
    print("")
    print("                    'Finalizar Login'")
    print("**********************************************************")


def Sobre():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |         |                 |     |")
    print("|HOME|                 |SOBRE NÓS|                 |LOGIN|")
    print("|    |                 |         |                 |     |")
    print("   Somos um restaurante de Comida Coreana\nServimos diferenciados pratos em nosso estabelecimento\nO melhor estabelecimento do Brasil de Culinaria Coreana")
    print("Para nos contatar utilize o numero de WhatsApp a baixo:\n               1999999-9999")
    print("**********************************************************")

