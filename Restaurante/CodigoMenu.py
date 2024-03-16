import InterfaceRestaurante

InterfaceRestaurante.Home()

while True:
    opcao = str(input("\nEscolha a opçao desejada: "))

    if opcao == "Home":
        InterfaceRestaurante.Home()
    elif opcao == "Cardapio":
        InterfaceRestaurante.Cardapio()
    elif opcao == "Sobre Nos" or opcao == "Sobre Nós":
        InterfaceRestaurante.Sobre()
    elif opcao == "Login":
        InterfaceRestaurante.Login() 
        try: 
            email=str(input("\nDigite Seu Email: "))
            if not email:
                raise ValueError("Erro Email")
            else:
                senha=str(input("\nDigite sua senha aqui: "))
                if not senha:
                    raise ValueError("Erro Senha")
        except ValueError as error:
            if str(error) == "Erro Email":
                print("Erro, Email Invalido")
            elif str(error) == "Erro Senha":
                print("Erro, Senha Invalida")
    elif opcao == "Principais":
        print("Futura parte pratos principais")
    elif opcao == "Porcoes" or opcao == "Porçoes":
        print("Futura parte de porcoes")