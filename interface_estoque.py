from Cadastrar import cadastrar_ing, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente, cadastrar_adm
from interface_restaurante import cardapio_adm
from Alterar import alterar_clientes, alterar_prato, alterar_fab, alterar_forn, alterar_func, alterar_adm
from Excluir import deletar_clientes, deletar_prato, deletar_fab, deletar_forn, deletar_func, deletar_login, deletar_ing, deletar_adm
from Listar import listar_login, listar_adm, listar_clientes, listar_fab, listar_forn, listar_func, listar_ing, listar_prato

def ger_logs():
    print("**********************************************************")
    print("                   JungKooking Estoque")
    print("")
    print("               |   1-Log De Auditoria   |")
    print("               |    2-Log De Acessos    |")
    print("               |   3-Ajuste de Cardapio |")
    print("**********************************************************")
    opcao=int(input("Escolha a opção desejada: "))
    if opcao==1:
        "printar log auditoria"
    elif opcao==2:
        "printar log acessos"
    elif opcao==3:
        cardapio_adm()

def pratos_cadastrados():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                |        |                |        |")
    print("|HOME|                |CARDAPIO|                |DESLOGAR|")
    print("|    |                |        |                |        |")
    print("Pratos Cadastrados")
    print("")
    print("BIBIMBAP")
    print("250g Carne Moida")
    print("300g Rabanete Coreano")
    print("300g Espinafre")
    print("200g Brotos Feijao Mungo")
    print("200g Cenoura")
    print("250g Abobrinha")
    print("200g Cogumelos shitake")
    print("400g Arroz de Sushi")
    print("4 ovos")
    print("")
    print("Custo Total:                                       R$27,00")
    print("Valor de Venda:                                    R$56,25")
    print("**********************************************************")

def estoque():
    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                |        |                |        |")
    print("|HOME|                |CARDAPIO|                |DESLOGAR|")
    print("|    |                |        |                |        |")
    print("Estoque de Ingredientes")
    print("")
    print("10kg Carne Moida")
    print("10kg Rabanete Coreano")
    print("10kg Espinafre")
    print("10kg Brotos Feijao Mungo")
    print("10kg Cenoura")
    print("10kg Abobrinha")
    print("10kg Cogumelos shitake")
    print("10kg Arroz de Sushi")
    print("100 ovos")
    print("**********************************************************")



