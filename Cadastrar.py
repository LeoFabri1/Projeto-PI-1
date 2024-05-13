from BancodeDados.banco_de_dados import conectar_bd
from BancodeDados.criptografia import cripto

def cadastrar_prato():
    print("****************************************************************************")
    print("Pratos")
    id_prato = int(input("Digite o id do prato: "))
    nome_prato = str(input("Digite o nome do prato: "))
    desc_prato = str(input("Digite a descricao do prato: "))
    categoria_prato = str(input("Digite aqui a categoria do prato: "))
    custo_prato = float(input("Digite o custo do prato: "))

    #pegar desc_prato e codificar
    desc_prato_cripto = cripto(desc_prato)

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Pratos (id_prato, nome_prato, desc_prato, categoria, custo_prato) VALUES (?, ?, ?, ?, ?)', (id_prato, nome_prato, desc_prato_cripto, categoria_prato, custo_prato))

    connection.commit()
    connection.close

def cadastrar_fab():
    print("****************************************************************************")
    print("Fabricante")
    id_fab = int(input("Digite o id do fabricante: "))
    nome_fab = str(input("Digite o nome do fabricante: "))
    tel_fab = int(input("Digite o telefone do fabricante: "))
    email_fab = str(input("Digite o email do fabricante: "))
    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fabricantes (id_fab, nome_fab, tel_fab, email_fab) VALUES (?, ?, ?, ?)', (id_fab, nome_fab, tel_fab, email_fab))

    connection.commit()
    connection.close

def cadastrar_forn():
    print("****************************************************************************")
    print("Fornecedor")
    id_forn = int(input("Digite o id do fornecedor: "))
    nome_forn = str(input("Digite o nome do fornecedor: "))
    tel_forn = int(input("Digite o telefone do fornecedor: "))
    email_forn = str(input("Digite o email do fornecedor: "))
    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fornecedores (id_forn, nome_forn, tel_forn, email_forn) VALUES (?, ?, ?, ?)', (id_forn, nome_forn, tel_forn, email_forn))

    connection.commit()
    connection.close

def cadastrar_func():
    print("****************************************************************************")
    print("Funcionario")
    aux_id_func = 0

    id_func = int(input("Digite o id do funcionario: "))
    nome_func = str(input("Digite o nome do funcionario: "))
    data_nasc_func = int(input("Digite a data de nascimento do funcionario: "))
    sal_func = float(input("Digite o salario do funcionario: "))
    data_contrato = int(input("Digite a data do contrato com o funcionario: "))
    categoria_func = str(input("Digite a categoria do funcionario: "))

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Funcionarios (id_func, nome_func, data_nasc_func, sal_func, data_contrato, categoria_func) VALUES (?, ?, ?, ?, ?, ?)', (id_func, nome_func, data_nasc_func, sal_func, data_contrato, categoria_func))

    connection.commit()
    connection.close

    id_login = int(input("Digite o id de login do funcionario: "))
    email_login = str(input("Digite o email de login do funcionario: "))
    senha_login = str(input("Digite a senha de login do funcionario: "))
    id_func = aux_id_func

    #senha funcionario criptografada
    senha_func_cripto = cripto(senha_login)

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_Func (id_login, email_login, senha_login, id_func) VALUES (?, ?, ?, ?)', (id_login, email_login, senha_func_cripto, aux_id_func))

    connection.commit()
    connection.close


def cadastrar_cliente():
    print("****************************************************************************")
    print("Usuario")
    id_cliente = int(input("Digite o id de login do cliente: "))
    nome_cliente = str(input("Digite o nome de login do cliente: "))
    email_cliente = str(input("Digite o email de login do cliente: "))
    senha_cliente = str(input("Digite a senha de login do cliente: "))

    #senha cliente criptografada
    senha_cliente_cripto = cripto(senha_cliente)

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_Clientes (id_cliente, nome_cliente, email_cliente, senha_cliente) VALUES (?, ?, ?, ?)', (id_cliente, nome_cliente, email_cliente, senha_cliente_cripto))

    connection.commit()
    connection.close

#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
#nao faco ideia de como faz isso 
def cadastrar_perm():
    print("****************************************************************************")
    print("Permissoes")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #descobrir como cadastrar permissões no banco
    cursor.execute('INSERT INTO () VALUES ()', ())

    connection.commit()
    connection.close