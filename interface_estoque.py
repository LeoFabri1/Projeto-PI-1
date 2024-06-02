from Cadastrar import cadastrar_ing, cadastrar_prato, cadastrar_fab, cadastrar_forn, cadastrar_func, cadastrar_cliente, cadastrar_adm
from BancodeDados.banco_de_dados import conectar_bd
from Alterar import alterar_clientes, alterar_prato, alterar_fab, alterar_forn, alterar_func, alterar_adm
from Excluir import deletar_clientes, deletar_prato, deletar_fab, deletar_forn, deletar_func, deletar_login, deletar_ing, deletar_adm
from Listar import listar_login, listar_adm, listar_clientes, listar_fab, listar_forn, listar_func, listar_ing, listar_prato_adm

def estoque():
    """PRINTA PAGINA DE ESTOQUE LISTANDO OS INGREDIENTES
    
    RETORNA:
    (listar_ing) = LISTA TODOS OS INGREDIENTES CONTIDOS NO ESTOQUE

    """

    print("**********************************************************")
    print("                   JungKooking Food")
    print("|    |                |        |                |        |")
    print("|HOME|                |CARDAPIO|                |DESLOGAR|")
    print("|    |                |        |                |        |")
    print("Estoque de Ingredientes")
    print("")
    listar_ing()