from BancodeDados.banco_de_dados import conectar_bd
from BancodeDados.criptografia import cripto

def cadastrar_ing():
    print("****************************************************************************")
    print("Cadastro de Ingredientes")
    #pega os dados
    nome_ing = str(input("Digite o nome do ingrediente: "))
    preco_ing = int(input("Digite o preço do ingrediente: "))
    fornecedor = int(input("Digite o id do fornecedor do ingrediente: "))
    fabricante = int(input("Digite o id do fabricante do ingrediente: "))
    quant_min = int(input("Digite a quantidade minima de estoque do ingrediente: "))
    quant_max = int(input("Digite a quantidade maxima de estoque do ingrediente: "))
    quant_est = int(input("Digite a quantidade do estoque do ingrediente: "))
    categoria = str(input("Digite a categoria do ingrediente: "))
    data_fab = input("Digite a data de fabricação do ingrediente: ")
    data_val = input("Digite a data de validade do ingrediente: ")

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Ingredientes (id_ing, nome_ing, preco_ing, fornecedor, fabricante, quant_min, quant_max, quant_est, categoria, data_fab, data_val) VALUES (seq_id_ing.NEXTVAL, :1, :2, :3, :4, :5, :6, :7, :8, :9, :10)', (nome_ing, preco_ing, fornecedor, fabricante, quant_min, quant_max, quant_est, categoria, data_fab, data_val))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_ing()

def cadastrar_prato():
    print("****************************************************************************")
    print("Cadastro de Pratos")
    #pega os dados
    nome_prato = str(input("Digite o nome do prato: "))
    desc_prato = str(input("Digite a descrição do prato: "))
    categoria_prato = str(input("Digite a categoria do prato: "))
    custo_prato = float(input("Digite o custo do prato: "))

    #criptografa a descrição do prato
    desc_prato_cripto = cripto(desc_prato)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Pratos (id_prato, nome_prato, desc_prato, categoria, custo_prato) VALUES (seq_id_prato.NEXTVAL, :1, :2, :3, :4)', (nome_prato, desc_prato_cripto, categoria_prato, custo_prato))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_prato()
#id = 2
#nome = Bibimbap
#desc = Uma tigela vibrante de arroz coberta com uma variedade de vegetais frescos, carne grelhada, ovo frito e gochujang. Misture todos os ingredientes para uma explosao de sabores e texturas. Uma refeicao coreana classica que equilibra perfeitamente o doce, o picante e o salgado em cada garfada.
#categoria = Prato Principal
#custo = 27

def cadastrar_fab():
    print("****************************************************************************")
    print("Fabricante")
    #pega os dados
    nome_fab = str(input("Digite o nome do fabricante: "))
    tel_fab = int(input("Digite o telefone do fabricante: "))
    email_fab = str(input("Digite o email do fabricante: "))

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fabricantes (id_fab, nome_fab, tel_fab, email_fab) VALUES (seq_id_fab.NEXTVAL, :1, :2, :3)', (nome_fab, tel_fab, email_fab))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_fab()

def cadastrar_forn():
    print("****************************************************************************")
    print("Fornecedor")
    #pega os dados
    nome_forn = str(input("Digite o nome do fornecedor: "))
    tel_forn = int(input("Digite o telefone do fornecedor: "))
    email_forn = str(input("Digite o email do fornecedor: "))
    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Fornecedores (id_forn, nome_forn, tel_forn, email_forn) VALUES (seq_id_forn.NEXTVAL, :1, :2, :3)', (nome_forn, tel_forn, email_forn))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_forn()

def cadastrar_func():
    print("****************************************************************************")
    print("Funcionario")
    #pega os dados
    nome_func = str(input("Digite o nome do funcionario: "))
    data_nasc_func = str(input("Digite a data de nascimento do funcionario: "))
    sal_func = float(input("Digite o salario do funcionario: "))
    data_contrato = str(input("Digite a data do contrato com o funcionario: "))
    categoria_func = str(input("Digite a categoria do funcionario: "))

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Funcionarios (id_func, nome_func, data_nasc_func, sal_func, data_contrato, categoria_func) VALUES (seq_id_func.NEXTVAL, :1, :2, :3, :4, :5)', (nome_func, data_nasc_func, sal_func, data_contrato, categoria_func))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

    email_login = str(input("Digite o email de login do funcionario: "))
    senha_login = str(input("Digite a senha de login do funcionario: "))
    id_func = int(input("Digite o id do funcionário do login a ser cadastrado:"))

    #senha funcionario criptografada
    senha_func_cripto = cripto(senha_login)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_Func (id_login, email_login, senha_login, id_func) VALUES (seq_id_login.NEXTVAL, :1, :2, :3)', (email_login, senha_func_cripto, id_func))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_func()

def cadastrar_cliente():
    print("****************************************************************************")
    print("Usuário")
    #pega os dados
    nome_cliente = str(input("Digite o nome de login do cliente: "))
    email_cliente = str(input("Digite o email de login do cliente: "))
    senha_cliente = str(input("Digite a senha de login do cliente: "))

    #senha cliente criptografada
    senha_cliente_cripto = cripto(senha_cliente)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_Clientes (id_cliente, nome_cliente, email_cliente, senha_cliente) VALUES (seq_id_cliente.NEXTVAL, :1, :2, :3)', (nome_cliente, email_cliente, senha_cliente_cripto))
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_cliente()

#adicionar adm
def cadastrar_adm():
    print("****************************************************************************")
    print("Administradores")
    #pega os dados
    id_func = int(input("Digite o id do funcionario a virar administrador: "))
    email_adm = str(input("Digite o email do administrador: "))
    senha_adm = str(input("Digite a senha do administrador: "))
    senha_cripto_adm = cripto(senha_adm)

    #adiciona ao banco
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Login_ADM (id_adm, email_adm, senha_adm, id_func) VALUES (seq_id_adm.NEXTVAL, :1, :2, :3)', (email_adm, senha_cripto_adm, id_func))
    id_func_del = id_func
    cursor.execute('DELETE FROM Login_Func WHERE id_func = :id_func_del', {'id_func_del': id_func_del})
    print("Cadastrado com sucesso!")

    connection.commit()
    connection.close()

#teste
#cadastrar_adm()