from Cadastrar import cadastrar_ing, cadastrar_adm, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente
from Alterar import alterar_login, alterar_ing, alterar_cliente, alterar_prato, alterar_fab, alterar_forn, alterar_func, alterar_adm
from Excluir import deletar_clientes, deletar_prato, deletar_fab, deletar_forn, deletar_func, deletar_login, deletar_ing, deletar_adm
from Listar import listar_login, listar_adm, listar_clientes, listar_fab, listar_forn, listar_func, listar_ing, listar_prato_adm
from Relatorios import gerar_relatorio_vendas, validar_data

def menu_adm():
    from interface_restaurante import home
    while True:
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
      opcao = input("Digite a opção desejada: ")

      if opcao == "1" or opcao == "Cadastrar":
        menu_adm_cadastro()
      elif opcao == "2" or opcao == "Alterar":
        menu_adm_altero()
      elif opcao == "3" or opcao == "Excluir":
        menu_adm_deleto()
      elif opcao == "4" or opcao == "Listar":
        menu_adm_listo()
      elif opcao == "5" or opcao == "Gerar Relatório" or "Relatório":
        menu_adm_relatorio()
      elif opcao == "6" or opcao == "Home":
        home()

def menu_adm_cadastro():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                     Menu Cadastros                      ")
    print("                                                         ")
    print("           |      1-Cadastrar Ingrediente    |           ")
    print("           |        2-Cadastrar Prato        |           ")
    print("           |      3-Cadastrar Fabricante     |           ")
    print("           |      4-Cadastrar Fornecedor     |           ")
    print("           |     5-Cadastrar Funcionário     |           ")
    print("           |        6-Cadastrar Cliente      |           ")
    print("           |    7-Cadastrar  Administrador   |           ")
    print("           |       8-Menu Administrador      |           ")
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
      cadastrar_func()
    elif opcao == 6:
      cadastrar_cliente()
    elif opcao == 7:
      cadastrar_adm()
    elif opcao == 8:
      menu_adm()

def menu_adm_altero():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Alterar                       ")
    print("                                                         ")
    print("            |      1-Alterar Ingrediente    |            ")
    print("            |        2-Alterar Prato        |            ")
    print("            |      3-Alterar Fabricante     |            ")
    print("            |      4-Alterar Fornecedor     |            ")
    print("            |     5-Alterar Funcionário     |            ")
    print("            |        6-Alterar Cliente      |            ")
    print("            |    7-Alterar  Administrador   |            ")
    print("            |  8-Alterar Login Funcionário  |            ")
    print("            |      9-Menu Administrador     |            ")
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
      alterar_func()
    elif opcao == 6:
      alterar_cliente()
    elif opcao == 7:
      alterar_adm()
    elif opcao == 8:
      alterar_login()
    elif opcao == 9:
      menu_adm()

def menu_adm_deleto():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Excluir                       ")
    print("                                                         ")
    print("            |      1-Excluir Ingrediente    |            ")
    print("            |        2-Excluir Prato        |            ")
    print("            |      3-Excluir Fabricante     |            ")
    print("            |      4-Excluir Fornecedor     |            ")
    print("            |     5-Excluir Funcionário     |            ")
    print("            |        6-Excluir Cliente      |            ")
    print("            |    7-Excluir  Administrador   |            ")
    print("            |  8-Excluir Login Funcionário  |            ")
    print("            |      9-Menu Administrador     |            ")
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
      deletar_func()
    elif opcao == 6:
      deletar_clientes()
    elif opcao == 7:
      deletar_adm()
    elif opcao == 8:
      deletar_login()
    elif opcao == 9:
      menu_adm()

def menu_adm_listo():
  while True:
    print("*********************************************************")
    print("        JungKooking Food - Estoque Administrador         ")
    print("                                                         ")
    print("                      Menu Listar                        ")
    print("                                                         ")
    print("            |      1-Listar Ingrediente    |             ")
    print("            |        2-Listar Prato        |             ")
    print("            |      3-Listar Fabricante     |             ")
    print("            |      4-Listar Fornecedor     |             ")
    print("            |     5-Listar Funcionário     |             ")
    print("            |        6-Listar Cliente      |             ")
    print("            |    7-Listar  Administrador   |             ")
    print("            |  8-Listar Login Funcionário  |             ")
    print("            |     9-Menu Administrador     |             ")
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
      listar_func()
    elif opcao == 6:
      listar_clientes()
    elif opcao == 7:
      listar_adm()
    elif opcao == 8:
      listar_login()
    elif opcao == 9:
      menu_adm()

#menu para o relatorio de vendas que esta no arquivo relatorios
def menu_adm_relatorio():
  while True:
    opcao=input("Deseja gerar o relatorio de vendas? (s/n): ")
    if opcao.lower()=='s':
      while True:
        data_venda=input("Digite a data que deseja acessar ao relatorio no formato AAAA-MM-DD: ")
        if validar_data(data_venda):
          gerar_relatorio_vendas(data_venda)
          break
        else:
        
          print("Formato de data invalido. pOR favor, digite a data no formato AAAA-MM-DD.")
    elif opcao.lower()=='n':
      print("Operaçao cancelada.")
      break
    else:
      print("Opçao invalida. Por favor digite 's' para sim ou 'n' para nao")