from BancodeDados.banco_de_dados import conectar_bd
from Listar import listar_login, listar_ing, listar_prato, listar_forn, listar_fab, listar_func, listar_adm, listar_clientes

def deletar_ing():
    print("****************************************************************************")
    print("Ingredientes")
    listar_ing()

    id_ing_del = input("Digite o id do ingrediente que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Ingredientes WHERE id_ing = :id_ing_del', {'id_ing_del': id_ing_del})

    connection.commit()
    connection.close()

#teste
#deletar_ing()

def deletar_prato():
    print("****************************************************************************")
    print("Pratos")
    listar_prato()

    id_prato_del = input("Digite o id do prato que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Pratos WHERE id_prato = :id_prato_del', {'id_prato_del': id_prato_del})

    connection.commit()
    connection.close()

#teste
#deletar_prato()

def deletar_fab():
    print("****************************************************************************")
    print("Fabricantes")
    listar_fab()

    id_fab_del = input("Digite o id do fabricante que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Fabricantes WHERE id_fab = :id_fab_del', {'id_fab_del': id_fab_del})

    connection.commit()
    connection.close()

#teste
#deletar_fab()

def deletar_forn():
    print("****************************************************************************")
    print("Fornecedores")
    listar_forn()

    id_forn_del = input("Digite o id do fornecedor que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Fornecedores WHERE id_forn = :id_forn_del', {'id_forn_del': id_forn_del})

    connection.commit()
    connection.close()

#teste
#deletar_forn()

def deletar_func():
    print("****************************************************************************")
    print("Funcionários")
    listar_func()

    id_func_del = input("Digite o id do funcionário que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Funcionarios WHERE id_func = :id_func_del', {'id_func_del': id_func_del})

    connection.commit()
    connection.close()

#teste
#deletar_func()

def deletar_clientes():
    print("****************************************************************************")
    print("Usuários")
    listar_clientes()

    id_cli_del = input("Digite o id do cliente que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_Clientes WHERE id_cliente = :id_cli_del', {'id_cli_del': id_cli_del})

    connection.commit()
    connection.close()

#teste
#deletar_clientes()

def deletar_login():
    print("****************************************************************************")
    print("Login Funcionários")
    listar_login()

    id_func_del = input("Digite o id do login que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_Func WHERE id_login = :id_func_del', {'id_func_del': id_func_del})

    connection.commit()
    connection.close()

#teste
#deletar_login()

def deletar_adm():
    print("****************************************************************************")
    print("Administradores")
    listar_adm()

    id_adm_del = input("Digite o id do administrador que deseja deletar: ")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM Login_ADM WHERE id_adm = :id_adm_del', {'id_adm_del': id_adm_del})

    connection.commit()
    connection.close()

#teste
#deletar_adm()