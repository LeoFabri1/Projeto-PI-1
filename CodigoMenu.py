import Interface

Interface.Home()

while True:
    opcao = str(input("\nEscolha a opçao desejada: "))

    if opcao == "Home":
        Interface.Home()
    elif opcao == "Cardapio":
        Interface.Cardapio()
    elif opcao == "Sobre Nos" or opcao == "Sobre Nós":
        Interface.Sobre()
    elif opcao == "Login":
        Interface.Login() 
        try: 
            email=str(input("\nDigite Seu Email: "))
            if email == "" or email == None:
                raise ValueError("Email Invalido")
        except ValueError as error:
            print(error)
    elif opcao == "Principais":
        print("Futura parte pratos principais")
    elif opcao == "Porcoes" or opcao == "Porçoes":
        print("Futura parte de porcoes")