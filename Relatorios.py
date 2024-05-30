from BancodeDados.banco_de_dados import conectar_bd
import datetime

def gerar_relatorio_vendas(data_venda):
    try:
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT TO_CHAR(pa.data_pagamento, 'YYYY-MM-DD') as data_pagamento, 
                   p.nome_prato, 
                   pa.valor_pagamento 
            FROM pratos p 
            JOIN pagamentos pa ON pa.id_prato = p.id_prato 
            WHERE pa.data_pagamento = TO_DATE(:data_venda, 'YYYY-MM-DD')
            """, {'data_venda': data_venda})
        vendas = cursor.fetchall()
        
        cursor.close()
        connection.close()

        # Adicionando depuração para verificar os dados recuperados
        print(f"Dados recuperados para a data {data_venda}: {vendas}")

        if not vendas:
            print(f"\nNão há lançamentos de vendas para a data: {data_venda}\n")
            return

        # Exibindo o relatório
        print(f"\nRelatório de Vendas - Data: {data_venda}\n")
        for venda in vendas:
            print(f"Data: {venda[0]}, Prato: {venda[1]}, Valor: {venda[2]}")

        # Calculando o total das vendas
        total_vendas = sum(venda[2] for venda in vendas)
        print(f"\nTotal de vendas: {total_vendas}")

    except Exception as e:
        print("\nErro ao gerar relatório de vendas:\n", e)

def validar_data(data):
    try:
        datetime.datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

data = input("Qual a data? \n")
if validar_data(data):
    gerar_relatorio_vendas(data)
else:
    print("Data inválida. Por favor, insira a data no formato YYYY-MM-DD.\n")