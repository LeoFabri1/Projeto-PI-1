from bancodedados.banco_de_dados import conectar_bd

def deletar_prato():
    print("****************************************************************************")
    print("Pratos")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from Pratos WHERE ...')

    connection.commit()
    connection.close

def deletar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from Fabricantes WHERE ...')

    connection.commit()
    connection.close

def deletar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from Fronecedores WHERE ...')

    connection.commit()
    connection.close

def deletar_func():
    print("****************************************************************************")
    print("Funcionario")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from Funcionarios WHERE ...')

    connection.commit()
    connection.close

def deletar_user():
    print("****************************************************************************")
    print("Usuario")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from Login_Clientes/Login_Func WHERE ...')

    connection.commit()
    connection.close

def deletar_perm():
    print("****************************************************************************")
    print("Permissoes")

    #deletar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('DELETE from ... WHERE ...')

    connection.commit()
    connection.close