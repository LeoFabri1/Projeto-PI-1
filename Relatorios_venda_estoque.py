from BancodeDados.banco_de_dados import conectar_bd
import datetime
from tabulate import tabulate
# pip install tabulate

def consultar_estoque():
    try:
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id_ing, nome_ing, quant_est, data_fab, data_val
            FROM Ingredientes
            """)
        estoque = cursor.fetchall()
        
        cursor.close()
        connection.close()

        # Adicionando depuração para verificar os dados recuperados
        print("\nDados recuperados do estoque:\n\n")
        print(tabulate(estoque, headers=["ID", "Nome", "Quantidade", "Data de Fabricação", "Data de Validade"], tablefmt="grid"))
        
    except Exception as e:
        print("\nErro ao consultar o estoque:\n", e)

# Chamando a função para consultar o estoque
consultar_estoque()

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

        

        if not vendas:
            print(f"\nNão há lançamentos de vendas para a data: {data_venda}\n")
            return

        # Definindo cabeçalho e linhas
        headers = ["Data", "Prato", "Valor"]
        
        # Calculando o total das vendas
        total_vendas = sum(venda[2] for venda in vendas)

        # Adicionando uma linha para o total na tabela
        vendas.append(("Total", "", total_vendas))

        # Exibindo o relatório
        print(f"\nRelatório de Vendas - Data: {data_venda}\n")
        print(tabulate(vendas, headers=headers, tablefmt="grid"))
    except Exception as e:
        print("\nErro ao gerar relatório de vendas:\n", e)

def validar_data(data):
    try:
        datetime.datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

data = input("\n\nQual a data a ser consultada?\nDigite no formato YYYY-MM-DD: ")
if validar_data(data):
    gerar_relatorio_vendas(data)
else:
    print("Data inválida. Por favor, insira a data no formato YYYY-MM-DD.\n")