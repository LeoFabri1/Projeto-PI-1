from Cadastrar import cadastrar_ing, cadastrar_adm, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente, cadastrar_adm
from interface_restaurante import cardapio_adm
from Alterar import alterar_clientes, alterar_prato, alterar_fab, alterar_forn, alterar_func, alterar_adm
from Excluir import deletar_clientes, deletar_prato, deletar_fab, deletar_forn, deletar_func, deletar_login, deletar_ing, deletar_adm
from Listar import listar_login, listar_adm, listar_clientes, listar_fab, listar_forn, listar_func, listar_ing, listar_prato

#Imprime o Menu de Cadastro
def cadastro():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |    1-Cadastrar Prato   |")
    print("               | 2-Cadastrar Fabricante |")
    print("               | 3-Cadastrar Fornecedor |")
    print("               | 4-Cadastrar Funcionario|")
    print("               |        5-Voltar        |")
    print("**********************************************************")
    
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        cadastrar_prato()
    elif opcao==2:
        cadastrar_fab()
    elif opcao==3:
        cadastrar_forn()
    elif opcao==4:
        cadastrar_func()
    elif opcao==5:
        cardapio_adm()

#Imprime o Menu Altera
def altero():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |     1-Alterar Prato    |")
    print("               |  2-Alterar Fabricante  |")
    print("               |  3-Alterar Fornecedor  |")
    print("               | 4-Alterar Funcionario  |")
    print("               |        5-Voltar        |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        alterar_prato()
    elif opcao==2:
        alterar_fab()
    elif opcao==3:
        alterar_forn()
    elif opcao==4:
        alterar_func()
    elif opcao==5:
        alterar_user()
    elif opcao==6:
        alterar_perm()

#Imprime o menu de Deleçao
def deleto():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |     1-Deletar prato    |")
    print("               |  2-Deletar Fabricante  |")
    print("               |  3-Deletar Fornecedor  |")
    print("               | 4-Deletar Funcionario  |")
    print("               |        5-Voltar        |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        deletar_prato()
    elif opcao==2:
        deletar_fab()
    elif opcao==3:
        deletar_forn()
    elif opcao==4:
        deletar_func()
    elif opcao==5:
        deletar_cliente()
    elif opcao ==6:
        deletar_perm()

#Imprime o menu de Filtragem
def filtro():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |     1-Filtrar prato      |")
    print("               |  2-Filtrar Fabricante    |")
    print("               |  3-Filtrar Fornecedor    |")
    print("               | 4-Filtrar Funcionario    |")
    print("               |   5-Filtrar Ingredientes |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        filtrar_prato()
    elif opcao==2:
        filtrar_fab()
    elif opcao==3:
        filtrar_forn()
    elif opcao==4:
        filtrar_func()
    elif opcao==5:
        filtrar_ingredientes()

def ger_user():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("*Printa Lista De Usuarios Existentes")
    print("               |     1-Adicionar User   |")
    print("               |     2-Alterar User     |")
    print("               |     3-Deletar User     |")
    print("               |   4-Ajuste de Cardapio |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao== "1" or opcao == "Adicionar":
        cadastrar_cliente()
    elif opcao == "2" or opcao == "Alterar":
        alterar_user()
    elif opcao == "3" or opcao == "Deletar":
        deletar_user()
    elif opcao == "4" or opcao == "Ajuste":
        cardapio_adm()

def ger_perm():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("*Printa Lista De Usuarios Existentes e suas permissoes atuais")
    print("               |  1-Adicionar Permissoes|")
    print("               |  2-Alterar Permissoes  |")
    print("               |  3-Deletar Permissoes  |")
    print("               |   4-Ajuste de Cardapio |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        cadastrar_perm()
    elif opcao==2:
        alterar_perm()
    elif opcao==3:
        deletar_perm()
    elif opcao==4:
        cardapio_adm()

def ger_logs():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |   1-Log De Auditoria   |")
    print("               |    2-Log De Acessos    |")
    print("               |   3-Ajuste de Cardapio |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        "printar log auditoria"
    elif opcao==2:
        "printar log acessos"
    elif opcao==3:
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
    print("**********************************************************")

    