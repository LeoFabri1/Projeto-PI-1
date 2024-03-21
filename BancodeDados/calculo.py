from bancodedados.banco_de_dados import conectar_bd

def obter_dados_produto():
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prato, nome_prato, desc_prato, custo_prato FROM Pratos')
    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return row

def inserir_resultados(codigo_produto, nome_produto, descricao_produto, custo_produto, preco_venda, total_despesas, valor_custo_fixo, comissao_vendas_reais, impostos_reais, receita_bruta, outros_custos, rentabilidade):
    connection = conectar_bd()
    cursor = connection.cursor()

    # Inserir na tabela
    cursor.execute('UPDATE Pratos SET preco_prato = :1, total_despesas = :2, valor_custo_fixo = :3, comissao_vendas = :4, impostos = :5, receita_bruta = :6, outros_custos = :7, rentabilidade = :8 WHERE id_prato = :9', (preco_venda, total_despesas, valor_custo_fixo, comissao_vendas_reais, impostos_reais, receita_bruta, outros_custos, rentabilidade, codigo_produto))

    # Commit da transação
    connection.commit()

    cursor.close()
    connection.close()

codigo_produto, nome_produto, descricao_produto, custo_produto = obter_dados_produto()

custo_fixo_porcentual = float(input("Digite o custo fixo/administrativo (%): "))
comissao_vendas_porcentual = float(input("Digite a comissão de vendas (%): "))
impostos_porcentual = float(input("Digite o imposto sobre a venda (%): "))
margem_lucro = float(input("Digite a margem de lucro (%): "))

# total das despesas
total_despesas = custo_fixo_porcentual + comissao_vendas_porcentual + impostos_porcentual + margem_lucro

#preço de venda
preco_venda = custo_produto / (1 - total_despesas / 100)

# conversao valor do custo fixo em reais
valor_custo_fixo = (custo_fixo_porcentual / 100) * preco_venda

# conversao valor da comissão de vendas em reais
comissao_vendas_reais = (comissao_vendas_porcentual / 100) * preco_venda

# conversaa valor dos impostos em reais
impostos_reais = (impostos_porcentual / 100) * preco_venda

#receita bruta
receita_bruta = preco_venda - custo_produto

#outros custos
outros_custos = valor_custo_fixo + comissao_vendas_reais + impostos_reais

#rentabilidade
rentabilidade = receita_bruta - outros_custos

#resultados
print("\nResultado do cadastro:")
print("Código do produto:", codigo_produto)
print("Nome do produto:", nome_produto)
print("Descrição do produto:", descricao_produto)

#Inserir os resultados no banco
inserir_resultados(codigo_produto, preco_venda, total_despesas, valor_custo_fixo, comissao_vendas_reais, impostos_reais, receita_bruta, outros_custos, rentabilidade)

#tbl de resultados
print("\nTabela de Resultados:")
print(f"A. Preço de Venda: {preco_venda:.2f} ({(preco_venda / preco_venda) * 100:.2f}%)")
print(f"B. Custo de Aquisição (Fornecedor): {custo_produto:.2f} ({(custo_produto / preco_venda) * 100:.2f}%)")
print(f"C. Receita Bruta (A-B): {receita_bruta:.2f} ({(receita_bruta / preco_venda) * 100:.2f}%)")
print(f"D. Custo Fixo/Administrativo: {valor_custo_fixo:.2f} ({(valor_custo_fixo / preco_venda) * 100:.2f}%)")
print(f"E. Comissão de Vendas: {comissao_vendas_reais:.2f} ({(comissao_vendas_reais / preco_venda) * 100:.2f}%)")
print(f"F. Impostos: {impostos_reais:.2f} ({(impostos_reais / preco_venda) * 100:.2f}%)")
print(f"G. Outros custos (D+E+F): {outros_custos:.2f} ({(outros_custos / preco_venda) * 100:.2f}%)")
print(f"H. Rentabilidade (C-G): {rentabilidade:.2f} ({(rentabilidade / preco_venda) * 100:.2f}%)")