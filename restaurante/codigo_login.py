from BancodeDados.banco_de_dados import conectar_bd
import interface_restaurante, codigo_menu
from BancodeDados.criptografia import descripto

def login_adm(senha, usuario):
    if usuario == "admin":
        try:
            conexao = conectar_bd()

            cursor = conexao.cursor()
            cursor.execute("SELECT senha_adm FROM Login_adm login WHERE usuario_adm = ?", ("admin"))
            resultado = cursor.fetchone()

            if resultado:
                senha_banco = resultado[0]
                if senha == descripto(senha_banco):
                    print("Login bem-sucedido como administrador.\n")
                    return interface_restaurante.cardapio_adm()
                else:
                    raise ValueError("Erro Senha")
            else:
                raise ValueError("Erro Usuario")

        except ValueError as error:
            print("Erro ao verificar login:", error)
        finally:
            if conexao:
                conexao.close()
    else:
        print("Usuário não é um administrador.")
        return codigo_menu.funcao_login()

