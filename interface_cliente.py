from BancodeDados.criptografia import descripto
from BancodeDados.banco_de_dados import conectar_bd
def menu_cliente():
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("|    |                 |        |                 |     |")
    print("|HOME|                 |CARDAPIO|                 |LOGIN|")
    print("|    |                 |        |                 |     |")
    print("CARDAPIO                                                 ")
    print("                                                         ")
    listar_prato_cliente()
    print("*********************************************************")

#pagina da comida do cardapio para adicionar ao carrinho
def escolher_prato():
    while True:
        prato_escolhido = input("Digite o nome do prato que deseja adicionar ao carrinho ou SAIR para voltar: ").strip()
        prato_esc = prato_escolhido.upper()

        if prato_esc == "SAIR":
            print("Voltando ao inicio...")
            break

        connection = conectar_bd()
        
        try:
            cursor = connection.cursor()
            query = 'SELECT * FROM PRATOS WHERE nome_prato = :nome_prato'
            cursor.execute(query, {"nome_prato": prato_escolhido})
            prato = cursor.fetchone()

            if prato:
                print("\nPrato escolhido:")
                print("Nome do Prato: ", prato[1])
                desc_descripto = descripto(prato[2])
                print("Descrição do Prato: ", desc_descripto)
                print("Categoria do Prato: ", prato[3])
                print("Valor do Prato: ", prato[5])
                print("")
                pagamento(prato[1], prato[5])
                break
            else:
                print("Prato não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            cursor.close()
            connection.close()

#pagina do pagamento
def pagamento(prato, preco):
    print("*********************************************************")
    print("                   JungKooking Food                      ")
    print("Endereço de entrega:                   Forma De Pagamento")
    print("CEP:                                                  Pix")
    print("Nome completo:                                     Cartao")
    print("Numero de Celular:                                       ")
    print("                                      Finalizar Pagamento")
    print("*********************************************************")
    
    celular = int(input("Digite aqui seu numero de celular: "))
    endereco = str(input("Digite aqui o endereco de entrega: "))
    data = input(str("Data Pagamento (AAAA-MM-DD): "))
    preco_prato = int(preco)
    nome_prato = prato
    pgto = str(input("Digite a forma de pagamento acima desejada (Pix ou Cartao): "))
    pag = pgto.upper()
    if pag == "PIX" or "CARTAO":
        print(f"Pagamento finalizado via {pag} com entrega no endereço {endereco}. Voce recebera um SMS de confirmacao no numero {celular}")
        connection = conectar_bd()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Pagamentos (id_pagamento, celular_cliente, data_pagamento, valor_pagamento, tipo_pagamento, prato_vendido) VALUES (seq_id_pag.NEXTVAL, :1, :2, :3, :4, :5)', (celular, data, preco_prato, pgto, nome_prato))
        
        cursor.close()
        connection.close()
    else:
        print("Forma de pagamento inválida. Por favor, escolha entre Pix ou Cartao.")

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