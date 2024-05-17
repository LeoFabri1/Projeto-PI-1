from interface_estoque import cadastro, altero, deleto, filtro
import menu_login
from BancodeDados.criptografia import cripto
from BancodeDados.banco_de_dados import conectar_bd
from Listar import listar_prato
import interface_adm

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
    listar_prato()
    print("*********************************************************")

#pagina da comida do cardapio para adicionar ao carrinho
def comida():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("KIMCHI")
    print("'FOTO'         Prato feito com acelga, gengibre e pimenta")
    print("Escolha abaixo a quantidade que deseja pedir: ")
    print("'Caixa de escolha'                                R$Valor")
    print("                                    Adicionar ao carrinho")
    print("*********************************************************")

#pagina do carrinho
def carrinho():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARRINHO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARRINHO")
    print("")
    print("Este são os itens que estao em seu carrinho:")
    print("Kimchi, 1 unidade  -  R$Valor")
    print("")
    print("                                         Subtotal:R$Valor")
    print("                                            Frete:R$Valor")
    print("                                            Total:R$Valor")
    print("                                         Finalizar pedido")
    print("*********************************************************")

#pagina do pagamento
def pagamento():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("Endereço de entrega:                   Forma De Pagamento")
    print("CEP:                                                  Pix")
    print("Nome completo:                      Cartao Credito/Debito")
    print("Numero de Celular:                                 Boleto")
    print("                                      Finalizar Pagamento")
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
    return menu_login.funcao_login()

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

#cadastro cliente
def cliente():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |         |                |     |")
    print("|HOME|                 |SOBRE NÓS|                |LOGIN|")
    print("|    |                 |         |                |     |")
    print("                                                         ")
    print("                 Cadastro de Cliente                     ")
    print("Digite seu nome:                                         ")
    print("Digite seu email:                                        ")
    print("Digite sua senha:                                        ")
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