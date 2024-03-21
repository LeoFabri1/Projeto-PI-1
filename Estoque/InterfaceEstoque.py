import Cadastrar, Excluir, Alterar, Filtrar
from Restaurante.InterfaceRestaurante import CardapioAdm

#Imprime o Menu de Cadastro
def Cadastro():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        Cadastrar.CadastrarPrato()
    elif(opcao==2):
        Cadastrar.CadastrarFab()
    elif(opcao==3):
        Cadastrar.CadastrarForn()
    elif(opcao==4):
        Cadastrar.CadastrarFunc()
    elif(opcao==5):
        CardapioAdm()

#Imprime o Menu Altera
def Altero():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        Alterar.AlterarPrato()
    elif(opcao==2):
        Alterar.AlterarFab()
    elif(opcao==3):
        Alterar.AlterarForn()
    elif(opcao==4):
        Alterar.AlterarFunc()
    elif(opcao==5):
        CardapioAdm()

#Imprime o menu de Deleçao
def Deleto():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        Excluir.DeletarPrato()
    elif(opcao==2):
        Excluir.DeletarFab()
    elif(opcao==3):
        Excluir.DeletarForn()
    elif(opcao==4):
        Excluir.DeletarFunc()
    elif(opcao==5):
        CardapioAdm()

#Imprime o menu de Filtragem
def Filtro():
    print("****************************************************************************")
    print("                              JungKooking Estoque")
    print("|        |     |            |     |            |     |             |     |      |")
    print("|1-Prato |     |2-Fabricante|     |3-Fornecedor|     |4-Funcionario|     |5-Menu|")
    print("|        |     |            |     |            |     |             |     |      |")
    opcao=int(input("Escolha a opção desejada: "))
    if(opcao==1):
        Filtrar.FiltrarPrato()
    elif(opcao==2):
        Filtrar.FiltrarFab()
    elif(opcao==3):
        Filtrar.FiltrarForn()
    elif(opcao==4):
        Filtrar.FiltrarFunc()
    elif(opcao==5):
        CardapioAdm()

CardapioAdm()