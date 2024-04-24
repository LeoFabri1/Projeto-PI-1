import interface_restaurante
import codigo_login

interface_restaurante.home()
def funcao_login():
    try: 
        usuario=str(input("\nDigite Seu Usuario: "))
        if not usuario:
            raise ValueError("Erro Usuario")
        else:
            senha=str(input("\nDigite sua senha aqui: "))
            if not senha:
                raise ValueError("Erro Senha")
            
        return codigo_login.login_adm(senha, usuario)

    except ValueError as error:
        if str(error) == "Erro Usuario":
            print("Erro, Usuario Invalido")
        elif str(error) == "Erro Senha":
            print("Erro, Senha Invalida")