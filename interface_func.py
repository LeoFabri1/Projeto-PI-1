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
      opcao = str(input("Digite a opção desejada: "))
      op = opcao.upper()

      if opcao == "1" or op == "CADASTRAR":
        menu_func_cadastro()
      elif opcao == "2" or op == "ALTERAR":
        menu_func_altero()
      elif opcao == "3" or op == "EXCLUIR":
        menu_func_deleto()
      elif opcao == "4" or op == "LISTAR":
        menu_func_listo()
      elif opcao == "5" or opcao == "HOME" or op == "SAIR":
        home()
      else:
        print("Opção inexistente.")

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
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      cadastrar_ing()
    elif opcao == "2" or op == "PRATO":
      cadastrar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      cadastrar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      cadastrar_forn()
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

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
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      alterar_ing()
    elif opcao == "2" or op == "PRATO":
      alterar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      alterar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      alterar_forn()
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

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
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      deletar_ing()
    elif opcao == "2" or op == "PRATO":
      deletar_prato()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      deletar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      deletar_forn()
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")

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
    opcao = str(input("Digite a opção desejada: "))
    op = opcao.upper()

    if opcao == "1" or op == "INGREDIENTE" or op == "ING":
      listar_ing()
    elif opcao == "2" or op == "PRATO":
      listar_prato_adm()
    elif opcao == "3" or op == "FABRICANTE" or op == "FAB":
      listar_fab()
    elif opcao == "4" or op == "FORNECEDOR" or op == "FORN":
      listar_forn()
    elif opcao == "5" or op == "HOME" or op == "SAIR":
      menu_func()
    else:
      print("Opção inexistente.")