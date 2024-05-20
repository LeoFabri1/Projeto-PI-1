from BancodeDados.banco_de_dados import conectar_bd
import datetime
# adicinar o id prato na tabela de pagamentos e coloca-la como foreign key para poder relcionar no relatorio de vendas
def gerar_relatorio_vendas(data_venda):
    try:
        
        connection = conectar_bd()
        cursor = connection.cursor()
        cursor.execute("SELECT p.nome_prato, pa.data_pagamento, pa.valor_pagamento FROM pratos p JOIN pagamentos pa ON pa.id_prato = p.id_prato WHERE pa.data_pagamento = :data_venda",{'data_venda' : data_venda})
        vendas = cursor.fetchall()
        cursor.close()
        connection.close()

        print("Relatório de Vendas - Data: ",data_venda)
        print("Data | Prato | Valor  | ")
        for venda in vendas:
            print(*venda, sep=" | ")
    except Exception as e:
        print("Erro ao gerar relatório de vendas:", e)



def validar_data(data):
    try:
        datetime.datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False



data_venda=input("Digite a data que deseja acesso ao relatorio no formato AAAA-MM-DD: ")
gerar_relatorio_vendas(data_venda)
       

