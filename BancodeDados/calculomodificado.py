from banco_de_dados import conectar_bd

custofixo = 3050
# Custo fixo = aluguel(1500)+salarios(1000)+serviços_publicos(300)+manutencao(200)+taxas_licenciamento_regulamentacao(50)

comissao_vendas_porcentual = 5
preco_venda=float(input("PREÇO DE VENDA DESEJADO: "))
custo_produto=float(input("CUSTO DO PRODUTO: "))


def obter_dados_produto():
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prato, nome_prato, desc_prato, custo_prato FROM Pratos')
    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return row

def inserir_resultados(id_prato, preco_venda, total_despesas, valor_custo_fixo, comissao_vendas_reais, impostos_reais, receita_bruta, outros_custos, rentabilidade):
    connection = conectar_bd()
    cursor = connection.cursor()

    # Inserir na tabela
    cursor.execute('UPDATE Pratos SET preco_prato = :1, total_despesas = :2, valor_custo_fixo = :3, comissao_vendas = :4, impostos = :5, receita_bruta = :6, outros_custos = :7, rentabilidade = :8 WHERE id_prato = :9', (preco_venda, total_despesas, valor_custo_fixo, comissao_vendas_reais, impostos_reais, receita_bruta, outros_custos, rentabilidade, id_prato))

    # Commit da transação
    connection.commit()

    cursor.close()
    connection.close()

id_prato, nome_prato, desc_prato, custo_prato = obter_dados_produto()


comissao_vendas_reais = (comissao_vendas_porcentual / 100) * preco_venda

custo_fixo_prato= custofixo/225
#aqui, supoe-se que venda 15 pratos de cada tipo dos 15 pratos presentes no cardapio ate o momento, logo 225 pratos vendidos por dia

imposto = 0.1*preco_venda 

outros_custos=comissao_vendas_reais+custo_fixo_prato+imposto+custo_produto

lucro = preco_venda-outros_custos

margem = lucro/100*custo_produto

# classificação do lucro
if margem > 20:
    classificacao_lucro = "Alto"
elif margem > 10:
    classificacao_lucro = "Lucro médio"
elif margem > 0:
    classificacao_lucro = "Lucro baixo"
else:
    classificacao_lucro = "Prejuízo"


print("\n    ****** Tabela de Resultados ******\n")
print("+---------------------------------------+")
print("|  Preço de Venda: {:.2f}              |".format(preco_venda))
print("|  Comissão de Vendas: {:.2f}            |".format(comissao_vendas_reais))
print("|  Impostos: {:.2f}                     |".format(imposto))
print("|  Outros Custos: {:.2f}                |".format(outros_custos))
print("|  Margem de Lucro: {:.2f}              |".format(margem))
print("|  Classificação do Lucro: {} |".format(classificacao_lucro))
print("+---------------------------------------+")