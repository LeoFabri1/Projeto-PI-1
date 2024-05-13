from Estoque.interface_estoque import cadastro, altero, deleto, filtro, ger_logs, ger_perm, ger_user
import codigo_menu
from BancodeDados.criptografia import cripto
from BancodeDados.banco_de_dados import conectar_bd
def home():
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
    while True:
        opcao = input("Digite a opcao desejada")

        if opcao.upper() == "HOME":
            home()
        elif opcao.upper() == "CARDAPIO":
            cardapio_cliente()
        elif opcao.upper() == "SOBRE NOS":
            sobre()
        elif opcao.upper() == "LOGIN":
            login()
        elif opcao == "13579":
            usuario = str(input("Digite o usuario de login do administrador para efetuar o cadastro de um novo administrador: "))
            senha = str(input("Digite a senha do administrador para efetuar o cadastro da mesma: "))
            senha_cripto = cripto(senha)

        #adicionar ao banco
        connection = conectar_bd()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Login_adm (usuario_adm, senha_adm) VALUES (?, ?)', (usuario, senha_cripto))

        connection.commit()
        connection.close

#Imprime A Pagina de Estoque
def cardapio_adm():
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
    print("               |   6-Gerenciar Usuarios |")
    print("               | 7-Gerenciar Permissoes |")
    print("               |    8-Vizualizar Logs   |")
    print("               |       9-Deslogar       |")
    print("**********************************************************")
    while True:
        opcao = input("Digite a opçao desejada")

        if opcao == "1" or opcao == "Adicionar Item":
            cadastro()
        elif opcao == "2" or opcao == "Alterar Item":
            altero()
        elif opcao == "3" or opcao == "Excluir Item":
            deleto()
        elif opcao == "4" or opcao == "Filtrar":
            filtro()
        elif opcao == "5" or opcao == "Ajuste Cardapio":
            cardapio_adm()
        elif opcao == "6" or opcao == "Gerenciar Usuarios":
            ger_user()
        elif opcao == "7" or opcao == "Gerenciar Permissoes":
            ger_perm()
        elif opcao == "8" or opcao == "Vizualizar Logs":
            ger_logs()
        elif opcao == "9" or opcao == "Deslogar":
            home()

def cardapio_cliente():
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

def comida():
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

def carrinho():
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

def pagamento():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("Endereço de entrega:                    Forma De Pagamento")
    print("CEP:                                                   Pix")
    print("Nome completo:                       Cartao Credito/Debito")
    print("Numero de Celular:                                  Boleto")
    print("                                       Finalizar Pagamento")
    print("**********************************************************")

def login():
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
    return codigo_menu.funcao_login()


def sobre():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                 |         |                 |     |")
    print("|HOME|                 |SOBRE NÓS|                 |LOGIN|")
    print("|    |                 |         |                 |     |")
    print("   Somos um restaurante de Comida Coreana\nServimos diferenciados pratos em nosso estabelecimento\nO melhor estabelecimento do Brasil de Culinaria Coreana")
    print("Para nos contatar utilize o numero de WhatsApp a baixo:\n               1999999-9999")
    print("**********************************************************")
