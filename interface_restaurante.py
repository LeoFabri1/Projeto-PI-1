import menu_login
from BancodeDados.criptografia import cripto, descripto
from BancodeDados.banco_de_dados import conectar_bd
from interface_cliente import listar_prato_cliente
from Cadastrar import cadastrar_cliente
#pagina inicial
def home():
    print("**********************************************************")
    print("                   JungKooking Food                       ")
    print("|    |        |        |        |         |        |     |")
    print("|HOME|        |CARDÁPIO|        |SOBRE NÓS|        |LOGIN|")
    print("|    |        |        |        |         |        |     |")
    print("                                                          ")
    print("EXPLORE SEU #MOMENTO COREANO                              ")
    print("                                                          ")
    print("      Pratos Principais           Porções(Acompanhamentos)")
    print("**********************************************************")
    while True:
        opcao = input("Digite a opção desejada")

        if opcao.upper() == "HOME":
            home()
        elif opcao.upper() == "CARDAPIO" or "CARDÁPIO":
            cardapio_cliente()
        elif opcao.upper() == "SOBRE NOS":
            sobre()
        elif opcao.upper() == "LOGIN":
            login_cadastro()

#pagina do cardapio
def cardapio_cliente():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARDAPIO                                                 ")
    print("                                                         ")
    listar_prato_cliente()
    print("*********************************************************")


#pagina escolha login ou cadastro
def login_cadastro():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|     |               |        |                   |    |")
    print("|LOGIN|               |CADASTRO|                   |HOME|")
    print("|     |               |        |                   |    |")
    print("                                                         ")
    print("                   |    1-Login    |                     ")
    print("                   |  2-Cadastro   |                     ")
    print("                   |     3-Home    |                     ")
    print("*********************************************************")
    while True:
        opcao = str(input("Digite a opcao desejada:"))
        if opcao == "1":
            return menu_login.funcao_login()
        if opcao == "2":
            return cadastrar_cliente()


#pagina sobre o restaurante
def sobre():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |         |                |     |")
    print("|HOME|                 |SOBRE NÓS|                |LOGIN|")
    print("|    |                 |         |                |     |")
    print("Somos um restaurante de Comida Coreana                   ")
    print("Servimos diferenciados pratos em nosso estabelecimento   ")
    print("O melhor estabelecimento do Brasil de Culinaria Coreana  ")
    print("Para nos contatar utilize o numero de WhatsApp a baixo:  ")
    print("                                             1999999-9999")
    print("*********************************************************")

def login():
    print("**********************************************************")
    print("                   JungKooking Food                       ")
    print("|    |                                          |        |")
    print("|HOME|                                          |CADASTRO|")
    print("|    |                                          |        |")
    print("                    ÁREA DE LOGIN                         ")
    print("Usuário: ")
    print("Senha: ")
    print("                                                          ")
    print("                    'Finalizar Login'                     ")
    print("**********************************************************")

def menu_adm():
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                  |    1-Cadastrar    |                  ")
    print("                  |     2-Alterar     |                  ")
    print("                  |     3-Excluir     |                  ")
    print("                  |      4-Listar     |                  ")
    print("                  | 5-Gerar Relatório |                  ")
    print("                  |       6-Home      |                  ")
    print("*********************************************************")
    while True:
        opcao = input("Digite a opção desejada: ")

        if opcao == "1" or opcao == "Cadastrar":
            interface_adm.menu_adm_cadastro()
        elif opcao == "2" or opcao == "Alterar":
            interface_adm.menu_adm_altero()
        elif opcao == "3" or opcao == "Excluir":
            interface_adm.menu_adm_deleto()
        elif opcao == "4" or opcao == "Listar":
            interface_adm.menu_adm_listo()
        elif opcao == "5" or opcao == "Gerar Relatório" or "Relatório":
            interface_adm.menu_adm_relatorio()
        elif opcao == "6" or opcao == "Home":
            home()