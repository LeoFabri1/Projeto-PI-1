from bancodedados.banco_de_dados import conectar_bd

def cadastrar_prato():
    print("****************************************************************************")
    print("Pratos")
    nome_prato = str(input("Digite o nome do prato:"))
    desc_prato = str(input("Digite a descricao do prato:"))
    preco_prato = float(input("Digite o preco de custo do prato:"))
    #definir uma aba em estoque para cadastrar os pratos, ingredientes, quantidades e valores
    #(bruto de cada ingrediente,prato e valor do prato com lucro)
    #definir os pratos com apenas a descricao e valor por item para os usuarios

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #mudar de acordo com input e banco de dados banco: id_prato, nome_prato, desc_prato, preco_prato, categoria, custo_prato, total_despesas
    cursor.execute('INSERT INTO Pratos (nome_prato, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close

def cadastrar_fab():
    print("****************************************************************************")
    print("Fabricante")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #mudar de acordo com input e banco de dados banco: id_fab, nome_fab, tel_fab, email_fab
    cursor.execute('INSERT INTO Fabricantes (nome_fab, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close

def cadastrar_forn():
    print("****************************************************************************")
    print("Fornecedor")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #mudar de acordo com input e banco de dados banco: id_forn, nome_forn, tel_forn, email_forn
    cursor.execute('INSERT INTO Fornecedores (nome_prato, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close

def cadastrar_func():
    print("****************************************************************************")
    print("Funcionario")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #mudar de acordo com input e banco de dados banco: id_func, nome_func, data_nasc_func, sal_func, data_contrato, categoria_func
    cursor.execute('INSERT INTO Funcionarios (nome_prato, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close

def cadastrar_user():
    print("****************************************************************************")
    print("Usuario")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #mudar de acordo com input e banco de dados banco: id_cliente, nome_cliente, email_cliente, senha_cliente
    #caso seja funcionario banco: id_login, email_login, senha_login, id_func
    cursor.execute('INSERT INTO Login_Clientes/Login_Func (nome_prato, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close

def cadastrar_perm():
    print("****************************************************************************")
    print("Permissoes")

    #adicionar ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    #descobrir como cadastrar permissões no banco
    cursor.execute('INSERT INTO Pratos (nome_prato, desc_prato, preco_prato) VALUES (?, ?, ?)', (nome_prato, desc_prato, preco_prato))

    connection.commit()
    connection.close