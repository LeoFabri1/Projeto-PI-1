from BancodeDados.banco_de_dados import conectar_bd

def alterar_prato():
    print("****************************************************************************")
    print("Pratos")

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from Pratos WHERE ...')

    connection.commit()
    connection.close

def alterar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from Fabricantes WHERE ...')

    connection.commit()
    connection.close

def alterar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from Fornecedores WHERE ...')

    connection.commit()
    connection.close

def alterar_func():
    print("****************************************************************************")
    print("Funcionario")

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from Funcionarios WHERE ...')

    connection.commit()
    connection.close

def alterar_user():
    print("****************************************************************************")
    print("Usuario")   

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from Login_Clientes/Login_Func WHERE ...')

    connection.commit()
    connection.close
    
def alterar_perm():
    print("****************************************************************************")
    print("Permissoes")

    #alterar dados do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('UPDATE from ... WHERE ...')

    connection.commit()
    connection.close