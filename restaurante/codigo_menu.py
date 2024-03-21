import interface_restaurante

interface_restaurante.home()

while True:
    opcao = str(input("\nEscolha a opçao desejada: "))

    if opcao == "Home":
        interface_restaurante.home()
    elif opcao == "Cardapio":
        interface_restaurante.cardapio_cliente()
    elif opcao == "Sobre Nos" or opcao == "Sobre Nós":
        interface_restaurante.sobre()
    elif opcao == "Login":
        interface_restaurante.login() 
        try: 
            usuario=str(input("\nDigite Seu Usuario: "))
            if not usuario:
                raise ValueError("Erro Usuario")
            #puxar FuncaoLogin.LoginAdm()
            else:
                senha=str(input("\nDigite sua senha aqui: "))
                if not senha:
                    raise ValueError("Erro Senha")
        except ValueError as error:
            if str(error) == "Erro Usuario":
                print("Erro, Usuario Invalido")
            elif str(error) == "Erro Senha":
                print("Erro, Senha Invalida")
    elif opcao == "Principais":
        print("Futura parte pratos principais")
    elif opcao == "Porcoes" or opcao == "Porçoes":
        print("Futura parte de porcoes")