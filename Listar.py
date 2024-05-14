from BancodeDados.banco_de_dados import conectar_bd
from BancodeDados.criptografia import descripto

def listar_prato():
    print("****************************************************************************")
    print("Pratos")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Pratos')

    resultados = cursor.fetchall()

    for prato in resultados:
        print("ID do Prato: ", prato[0])
        print("Nome do Prato: ", prato[1])
        desc_descripto = descripto(prato[2])
        print("Descrição do Prato: ", desc_descripto)
        print("Categoria do Prato: ", prato[3])
        print("Preço Custo do Prato: ", prato[4])
    
    cursor.close()
    connection.close()

#teste
listar_prato()

def listar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Fabricantes')
    resultados = cursor.fetchall()

    for fab in resultados:
        print("ID do Fabricante: ", fab[0])
        print("Nome do Fabricante: ", fab[1])
        print("Email do Fabricante: ", fab[2])
        print("Telefone do Fabricante: ", fab[3])
    
    cursor.close()
    connection.close()

#teste
#listar_fab()

def listar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Fornecedores')
    resultados = cursor.fetchall()

    for forn in resultados:
        print("ID do Fornecedor: ", forn[0])
        print("Nome do Fornecedor: ", forn[1])
        print("Email do Fornecedor: ", forn[2])
        print("Telefone do Fornecedor: ", forn[3])
    
    cursor.close()
    connection.close()

#teste
#listar_forn()

def listar_func():
    print("****************************************************************************")
    print("Funcionario")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Funcionarios')
    resultados = cursor.fetchall()

    for func in resultados:
        print("ID do Funcionário: ", func[0])
        print("Nome do Funcionário: ", func[1])
        print("Data do Nascimento do Funcionário: ", func[2])
        print("Salário do Funcionário: ", func[3])
        print("Data de Contrato do Funcionário: ", func[4])
        print("Categoria do Funcionário: ", func[5])
    
    cursor.close()
    connection.close()

#teste
#listar_func()