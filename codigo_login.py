from BancodeDados.banco_de_dados import conectar_bd
from interface_adm import menu_adm
from interface_func import menu_func
from interface_cliente import menu_cliente
from BancodeDados.criptografia import descripto
from logs import log_auditoria, log_accesso

def login_adm(senha, usuario):
    from menu_login import funcao_login
    try:
        email = usuario
        senhaver = senha.upper()
        connection = conectar_bd()
        #verifica se é adm
        cursor = connection.cursor()
        cursor.execute('SELECT id_adm, senha_adm FROM Login_ADM login WHERE email_adm = :email', {'email': email})
        resultadoadm = cursor.fetchone()
        #verifica se tem no banco
        if resultadoadm:
            id_adm, senha_adm_cripto = resultadoadm
            senha_adm = descripto(senha_adm_cripto)
            #verifica se senha está correta
            if senhaver == senha_adm:
                print("Login de administrador bem-sucedido!")
                log_auditoria(connection, "admin", id_adm, "login")
                cursor.close()
                connection.close()
                menu_adm()
            else:
                print("Senha de administrador incorreta.")
                cursor.close()
                connection.close()
                funcao_login()
        else:
            #verifica se é funcionario
            cursor.execute('SELECT id_login, senha_login FROM Login_Func WHERE email_login = :email', {'email': email})
            resultadofunc = cursor.fetchone()
            #verifica se tem no banco
            if resultadofunc:
                id_func, senha_func_cripto = resultadofunc
                senha_func = descripto(senha_func_cripto)
                #verifica se senha está correta
                if senhaver == senha_func:
                    print("Login de funcionário bem-sucedido!")
                    log_auditoria(connection, "funcionario", id_func, "login")
                    cursor.close()
                    connection.close()
                    menu_func()
                else:
                    print("Senha de funcionário incorreta.")
                    cursor.close()
                    connection.close()
                    funcao_login()
            else:
                #verifica se é cliente
                cursor.execute('SELECT id_cliente, senha_cliente, nome_cliente FROM login_clientes WHERE email_cliente = :email', {'email': email})
                resultadocliente = cursor.fetchone()
                #verifica se tem no banco
                if resultadocliente:
                    id_cliente, senha_cli_cripto, nome_cliente = resultadocliente
                    senha_cli = descripto(senha_cli_cripto)
                    #verifica se senha está correta
                    if senhaver == senha_cli:
                        print(f"Login bem-sucedido! Bem-vindo, {nome_cliente}")
                        log_accesso(connection, "cliente", id_cliente, email, "login")
                        cursor.close()
                        connection.close()
                        menu_cliente()
                    else:
                        print("Senha de cliente incorreta.")
                        cursor.close()
                        connection.close()
                        funcao_login()
                #caso n ache nenhum cadastro imprime mensagem
                else:
                    print("Nenhum cadastro encontrado com esse email, tente novamente.")
                    cursor.close()
                    connection.close()
                    funcao_login()
    except ValueError as error:
        print("Erro ao verificar login:", error)