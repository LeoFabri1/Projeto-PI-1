import menu_login
from interface_cliente import listar_prato_cliente
from Cadastrar import cadastrar_cliente
#pagina inicial
def home():
    while True:
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
        opcao = input("Digite a opção desejada ou sair: ").strip().upper()

        if opcao == "HOME":
            continue
        elif opcao in ("CARDAPIO", "CARDÁPIO"):
            cardapio_cliente()
        elif opcao in ("SOBRE NOS", "SOBRE"):
            sobre()
        elif opcao == "LOGIN":
            login_cadastro()
        elif opcao == "SAIR":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

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
    while True:
        print("*********************************************************")
        print("                   JungKooking Food                      ")
        print("|     |               |        |                   |    |")
        print("|LOGIN|               |CADASTRO|                   |HOME|")
        print("|     |               |        |                   |    |")
        print("                                                         ")
        print("                   |    1-Login    |                     ")
        print("                   |  2-Cadastro   |                     ")
        print("                   |     3-Home    |                     ")
        print("                   |     4-Sair    |                     ")
        print("*********************************************************")
        opcao = str(input("Digite a opcao desejada: "))
        if opcao == "1":
            menu_login.funcao_login()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            home()
        elif opcao == "4":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida, tente novamente.")

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

#pagina login
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