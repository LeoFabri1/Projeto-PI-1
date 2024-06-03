import codigo_login

#login adm
#testeadm@gmail.com
#senhaadm
#login cliente
#testecliente@gmail.com
#senhacliente
#login func
#testefunc@gmail.com
#senhatestefunc

def funcao_login():
    try: 
        usuario=str(input("\nDigite o email do usuário: "))
        if not usuario:
            raise ValueError("Erro Usuario")
        else:
            senha=str(input("\nDigite sua senha aqui: "))
            if not senha:
                raise ValueError("Erro Senha")
                
        return codigo_login.login_adm(senha, usuario)

    except ValueError as error:
        if str(error) == "Erro Usuario":
            print("Erro: Usuario Inválido")
        elif str(error) == "Erro Senha":
            print("Erro, Senha Invalida")