import InterfaceEstoque

InterfaceEstoque.Login()

email=str(input("Email: "))
senha=str(input("Senha: "))
print("**********************************************************")

#verificar se email e senha corretos do banco de dados
#tabela login (id_login, email_login, senha_login, id_func(fk))