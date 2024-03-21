import cadastrar, excluir, alterar, filtrar
from restaurante.interface_restaurante import cardapio_adm

#Imprime o Menu de Cadastro
def cadastro():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        cadastrar.cadastrar_prato()
    elif(opcao==2):
        cadastrar.cadastrar_fab()
    elif(opcao==3):
        cadastrar.cadastrar_forn()
    elif(opcao==4):
        cadastrar.cadastrar_func()
    elif(opcao==5):
        cardapio_adm()

#Imprime o Menu Altera
def altero():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        alterar.alterar_prato()
    elif(opcao==2):
        alterar.alterar_fab()
    elif(opcao==3):
        alterar.alterar_forn()
    elif(opcao==4):
        alterar.alterar_forn()
    elif(opcao==5):
        cardapio_adm()

#Imprime o menu de Deleçao
def deleto():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        excluir.deletar_prato()
    elif(opcao==2):
        excluir.deletar_fab()
    elif(opcao==3):
        excluir.deletar_forn()
    elif(opcao==4):
        excluir.deletar_func()
    elif(opcao==5):
        cardapio_adm()

#Imprime o menu de Filtragem
def filtro():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        filtrar.filtrar_prato()
    elif(opcao==2):
        filtrar.filtrar_fab()
    elif(opcao==3):
        filtrar.filtrar_forn()
    elif(opcao==4):
        filtrar.filtrar_func()
    elif(opcao==5):
        cardapio_adm()

cardapio_adm()