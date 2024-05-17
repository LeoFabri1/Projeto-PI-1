from BancodeDados.banco_de_dados import conectar_bd
from interface_adm import menu_adm
from interface_func import menu_func
from interface_cliente import menu_cliente
from menu_login import funcao_login
from BancodeDados.criptografia import descripto

def login_adm(senha, usuario):
    try:
        email = usuario
        connection = conectar_bd()
        #verifica se é adm
        cursor = connection.cursor()
        cursor.executecursor.execute('SELECT senha_adm FROM Login_ADM login WHERE email_adm = :email', {'email': email})
        resultadoadm = cursor.fetchone()
        #verifica se tem no banco
        if resultadoadm:
            senha_adm = descripto(resultadoadm[0])
            #verifica se senha está correta
            if senha == senha_adm:
                print("Login de administrador bem-sucedido!")
                cursor.close()
                connection.close()
                return menu_adm()
            else:
                print("Senha de administrador incorreta.")
                cursor.close()
                connection.close()
                return funcao_login()
        else:
            #verifica se é funcionario
            cursor.execute('SELECT senha_login FROM Login_Func WHERE email_func = :email', {'email': email})
            resultadofunc = cursor.fetchone()
            #verifica se tem no banco
            if resultadofunc:
                senha_func = descripto(resultadofunc[0])
                #verifica se senha está correta
                if senha == senha_func:
                    print("Login de funcionário bem-sucedido!")
                    cursor.close()
                    connection.close()
                    return menu_func()
                else:
                    print("Senha de funcionário incorreta.")
                    cursor.close()
                    connection.close()
                    return funcao_login()
            else:
                #verifica se é cliente
                cursor.execute('SELECT senha_cliente FROM Login_Clientes WHERE email_cliente = :email', {'email': email})
                resultadocliente = cursor.fetchone()
                #verifica se tem no banco
                if resultadocliente:
                    senha_cli = descripto(resultadocliente[0])
                    #verifica se senha está correta
                    if senha == senha_cli:
                        print("Login de cliente bem-sucedido!")
                        cursor.close()
                        connection.close()
                        return menu_cliente()
                    else:
                        print("Senha de cliente incorreta.")
                        cursor.close()
                        connection.close()
                        return funcao_login()
                #caso n ache nenhum cadastro imprime mensagem
                else:
                    print("Nenhum cadastro encontrado com esse email, tente novamente.")
                    cursor.close()
                    connection.close()
                    return funcao_login()
    except ValueError as error:
        print("Erro ao verificar login:", error)