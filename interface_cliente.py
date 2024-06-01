from BancodeDados.criptografia import descripto
from BancodeDados.banco_de_dados import conectar_bd
def menu_cliente():
  print("Menu Cliente")

#pagina da comida do cardapio para adicionar ao carrinho
def escolher_prato():
    prato_escolhido = input("Digite o nome do prato que deseja adicionar ao carrinho: ")

    connection = conectar_bd()
    
    cursor = connection.cursor()
    query = 'SELECT * FROM PRATOS WHERE nome_prato = :nome_prato'
    cursor.execute(query, nome_prato=prato_escolhido)
    prato = cursor.fetchone()

    if prato:
        print("\nPrato escolhido:")
        print("Nome do Prato: ", prato[1])
        desc_descripto = descripto(prato[2])
        print("Descrição do Prato: ", desc_descripto)
        print("Categoria do Prato: ", prato[3])
        print("Valor do Prato: ", prato[5])
        print("")
        pagamento()
    else:
        print("Prato não encontrado.")

    cursor.close()
    connection.close()

#pagina do pagamento
def pagamento():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("Endereço de entrega:                   Forma De Pagamento")
    print("CEP:                                                  Pix")
    print("Nome completo:                                     Cartao")
    print("Numero de Celular:                                       ")
    print("                                      Finalizar Pagamento")
    print("*********************************************************")
    
    celular = int(input("Digite aqui seu numero de celular:"))
    endereco = str(input("Digite aqui o endereco de entrega:"))
    pgto = str(input("Digite a forma de pagamento acima desejada (Pix ou Cartao):"))
    if pgto != "Pix" or "pix" and pgto != "Cartao" or "cartao":
        print("Forma de pagamento inválida. Por favor, escolha entre Pix ou Cartao.")
    else:
      print(f"Pagamento finalizado via {pgto} com entrega no endereço {endereco}. Voce recebera um SMS de confirmacao no numero {celular}")
    


def listar_prato_cliente():
    print("****************************************************************************")
    print("Pratos")

    #buscar do banco de dados
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT * from Pratos ORDER BY id_prato')

    resultados = cursor.fetchall()

    for prato in resultados:
        print("Nome do Prato: ", prato[1])
        desc_descripto = descripto(prato[2])
        print("Descrição do Prato: ", desc_descripto)
        print("Categoria do Prato: ", prato[3])
        print("Valor do Prato: ", prato[5])
    
    cursor.close()
    connection.close()
    escolher_prato()

listar_prato_cliente()