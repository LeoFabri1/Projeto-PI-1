from interface_restaurante import home, login
import codigo_login
from Cadastrar import cadastrar_cliente

home()
def funcao_login():
    try: 
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            login()
            usuario=str(input("\nDigite o email do usuário: "))
            if not usuario:
                raise ValueError("Erro Usuario")
            else:
                senha=str(input("\nDigite sua senha aqui: "))
                if not senha:
                    raise ValueError("Erro Senha")
                
            return codigo_login.login_adm(senha, usuario)
        elif opcao == 2:
            cadastrar_cliente()
        else:
            home()

    except ValueError as error:
        if str(error) == "Erro Usuario":
            print("Erro: Usuario Inválido")
        elif str(error) == "Erro Senha":
            print("Erro, Senha Invalida")

