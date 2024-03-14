import Interface
Interface.Home
while True:
    opcao = str(input("\nEscolha a opçao desejada: "))

    if opcao == "Home":
        Interface.Home()
    elif opcao == "Cardapio":
        Interface.Cardapio()
    elif opcao == "Sobre Nos" or "Sobre Nós":
        Interface.Sobre()
    elif opcao == "Login":
        print("Funcao ainda nao adicionada")
    elif opcao == "Principais":
        print("Futura parte pratos principais")
    elif opcao == "Porcoes" or "Porçoes":
        print("Futura parte de porcoes")