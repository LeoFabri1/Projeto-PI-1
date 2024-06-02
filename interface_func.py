from Cadastrar import cadastrar_ing, cadastrar_prato, cadastrar_fab, cadastrar_forn
from Alterar import alterar_ing, alterar_prato, alterar_fab, alterar_forn
from Excluir import deletar_prato, deletar_fab, deletar_forn, deletar_ing
from Listar import listar_fab, listar_forn, listar_ing, listar_prato_adm

def menu_func():
    from interface_restaurante import home
    while True:
      print("*********************************************************")
      print("        JungKooking Food - Estoque Funcionário           ")
      print("                                                         ")
      print("                  |    1-Cadastrar    |                  ")
      print("                  |     2-Alterar     |                  ")
      print("                  |     3-Excluir     |                  ")
      print("                  |      4-Listar     |                  ")
      print("                  |       5-Home      |                  ")
      print("*********************************************************")
      opcao = input("Digite a opção desejada: ")

      if opcao == "1" or opcao == "Cadastrar":
        menu_func_cadastro()
      elif opcao == "2" or opcao == "Alterar":
        menu_func_altero()
      elif opcao == "3" or opcao == "Excluir":
        menu_func_deleto()
      elif opcao == "4" or opcao == "Listar":
        menu_func_listo()
      elif opcao == "5" or opcao == "Home":
        home()

def menu_func_cadastro():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                     Menu Cadastros                      ")
    print("                                                         ")
    print("           |      1-Cadastrar Ingrediente    |           ")
    print("           |        2-Cadastrar Prato        |           ")
    print("           |      3-Cadastrar Fabricante     |           ")
    print("           |      4-Cadastrar Fornecedor     |           ")
    print("           |        5-Menu Funcionário       |           ")
    print("*********************************************************")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      cadastrar_ing()
    elif opcao == 2:
      cadastrar_prato()
    elif opcao == 3:
      cadastrar_fab()
    elif opcao == 4:
      cadastrar_forn()
    elif opcao == 5:
      menu_func()

def menu_func_altero():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Alterar                       ")
    print("                                                         ")
    print("            |      1-Alterar Ingrediente    |            ")
    print("            |        2-Alterar Prato        |            ")
    print("            |      3-Alterar Fabricante     |            ")
    print("            |      4-Alterar Fornecedor     |            ")
    print("            |       5-Menu Funcionário      |            ")
    print("*********************************************************")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      alterar_ing()
    elif opcao == 2:
      alterar_prato()
    elif opcao == 3:
      alterar_fab()
    elif opcao == 4:
      alterar_forn()
    elif opcao == 5:
      menu_func()

def menu_func_deleto():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Excluir                       ")
    print("                                                         ")
    print("            |      1-Excluir Ingrediente    |            ")
    print("            |        2-Excluir Prato        |            ")
    print("            |      3-Excluir Fabricante     |            ")
    print("            |      4-Excluir Fornecedor     |            ")
    print("            |       5-Menu Funcionário      |            ")
    print("*********************************************************")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      deletar_ing()
    elif opcao == 2:
      deletar_prato()
    elif opcao == 3:
      deletar_fab()
    elif opcao == 4:
      deletar_forn()
    elif opcao == 5:
      menu_func()

def menu_func_listo():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Funcionário           ")
    print("                                                         ")
    print("                      Menu Listar                        ")
    print("                                                         ")
    print("            |      1-Listar Ingrediente    |             ")
    print("            |        2-Listar Prato        |             ")
    print("            |      3-Listar Fabricante     |             ")
    print("            |      4-Listar Fornecedor     |             ")
    print("            |       5-Menu Funcionário     |            ")
    print("*********************************************************")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      listar_ing()
    elif opcao == 2:
      listar_prato_adm()
    elif opcao == 3:
      listar_fab()
    elif opcao == 4:
      listar_forn()
    elif opcao == 5:
      menu_func()