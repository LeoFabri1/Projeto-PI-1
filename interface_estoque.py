from Cadastrar import cadastrar_ing, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente, cadastrar_adm
from interface_restaurante import cardapio_adm
from BancodeDados.banco_de_dados import conectar_bd
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
    connection = conectar_bd()
    cursor = connection.cursor()

    nome_tabela = "INGREDIENTES"

    query = f"SELECT ID_ING, NOME_ING, PRECO_ING, FORNECEDOR, FABRICANTE, QUANT_EST, CATEGORIA, DATA_FAB, DATA_VAL FROM {nome_tabela}"

    cursor.execute(query)

    for row in cursor:
        id_ing, nome_ing, preco_ing, fornecedor, fabricante, quant_est, categoria, data_fab, data_val = row
        print(f"INGREDIENTE: {id_ing}")
        print(f"Fornecedor: {fornecedor}")
        print(f"Fabricante: {fabricante} Fabricado em {data_fab.strftime('%d/%m/%Y')}")
        print(f"Categoria do produto: {categoria}")
        print(f"{quant_est}kg {nome_ing}: Preço Por KG: R${preco_ing}")
        print(f"Vencimento do Lote: {data_val.strftime('%d/%m/%Y')}")
        print("")
        print("**********************************************************")

    cursor.close()
    connection.close()




