from BancodeDados.banco_de_dados import conectar_bd
from BancodeDados.criptogradia import descripto

def filtrar_prato():
    print("****************************************************************************")
    print("Pratos")

    #filtrar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT from Pratos WHERE ...')

    resultados = cursor.fetchall()

    desc_prato = descripto(resultados)

    print(desc_prato)
    
    cursor.close
    connection.close

def filtrar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #filtrar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT from Fabricantes WHERE ...')

    connection.commit()
    connection.close

def filtrar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #filtrar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT from Fornecedores WHERE ...')

    connection.commit()
    connection.close

def filtrar_func():
    print("****************************************************************************")
    print("Funcionario")

    #filtrar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT from Funcionarios WHERE ...')

    connection.commit()
    connection.close

