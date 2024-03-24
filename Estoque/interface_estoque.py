import cadastrar, excluir, alterar, filtrar
from restaurante.interface_restaurante import cardapio_adm

#Imprime o Menu de Cadastro
def cadastro():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    print("****************************************************************************")
    
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
    print("****************************************************************************")
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
    print("****************************************************************************")
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
    print("Filtrar")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    print("****************************************************************************")
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

def pratos_cadastrados():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                |        |                |        |")
    print("|HOME|                |CARDAPIO|                |DESLOGAR|")
    print("|    |                |        |                |        |")
    print("Pratos Cadastrados")
    print("")
    print("BIBIMBAP")
    print("250g Carne Moida")
    print("300g Rabanete Coreano")
    print("300g Espinafre")
    print("200g Brotos Feijao Mungo")
    print("200g Cenoura")
    print("250g Abobrinha")
    print("200g Cogumelos shitake")
    print("400g Arroz de Sushi")
    print("4 ovos")
    print("")
    print("Custo Total:                                       R$27,00")
    print("Valor de Venda:                                    R$56,25")
    print("**********************************************************")

def estoque():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                |        |                |        |")
    print("|HOME|                |CARDAPIO|                |DESLOGAR|")
    print("|    |                |        |                |        |")
    print("Estoque de Ingredientes")
    print("")
    print("10kg Carne Moida")
    print("10kg Rabanete Coreano")
    print("10kg Espinafre")
    print("10kg Brotos Feijao Mungo")
    print("10kg Cenoura")
    print("10kg Abobrinha")
    print("10kg Cogumelos shitake")
    print("10kg Arroz de Sushi")
    print("100 ovos")