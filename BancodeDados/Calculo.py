from banco_de_dados import conectar_bd

custofixo = 3050
# Custo fixo = aluguel(1500)+salarios(1000)+serviços_publicos(300)+manutencao(200)+taxas_licenciamento_regulamentacao(50)

id=int(input("Qual id do prato deseja modificar? "))
preco_venda=float(input("PREÇO DE VENDA DESEJADO: "))
custo_produto=float(input("CUSTO DO PRODUTO: "))


def obter_dados_produto():
    connection = conectar_bd()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prato, nome_prato, desc_prato, custo_prato FROM Pratos')
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

def inserir_resultados(id_prato, preco_venda, custo_fixo, imposto, margem):
    connection = conectar_bd()
    cursor = connection.cursor()

    # Inserir na tabela
    cursor.execute('UPDATE Pratos SET preco_venda = :1, custo_fixo = :2, impostos = :3, margem_lucro = :4 WHERE id_prato = :5', (preco_venda, custo_fixo, imposto, margem, id_prato))

    # Commit da transação
    connection.commit()

    cursor.close()
    connection.close()
# Obtém os dados dos produtos
dados_produtos = obter_dados_produto()

# Flag para verificar se o item foi encontrado
item_encontrado = False

# Dicionário de cores para classificação de lucro
cores = {
    "Alto": "\033[92m",  # Verde
    "Lucro médio": "\033[93m",  # Amarelo
    "Lucro baixo": "\033[91m",  # Vermelho
    "Prejuízo": "\033[91m"  # Vermelho
}

# Reseta a cor após o texto ser exibido
reset_cor = "\033[0m"

# Processa cada produto individualmente
for produto in dados_produtos:
    id_prato, nome_prato, desc_prato, custo_prato = produto
    
    # Verifica se o ID do produto corresponde ao ID desejado
    if id_prato == id:
        item_encontrado = True

        # Cálculo específico para este produto
        custo_fixo_prato = custofixo / 225
        imposto = 0.1 * preco_venda
        outros_custos = custo_fixo_prato + imposto + custo_produto
        lucro = preco_venda - outros_custos
        margem = (lucro / preco_venda)*100

        # classificação do lucro
        if margem > 20:
            classificacao_lucro = "Alto"
        elif margem > 10:
            classificacao_lucro = "Lucro médio"
        elif margem > 0:
            classificacao_lucro = "Lucro baixo"
        else:
            classificacao_lucro = "Prejuízo"

        # Exibe a classificação de lucro com a cor apropriada
        classificacao_formatada = cores.get(classificacao_lucro, "") + classificacao_lucro + reset_cor

        print("\n    ****** Tabela de Resultados ******\n")
        print("+-------------------------------------------------+")
        print("| {:<15} | {:<13} | {:<11} |".format("Preço de Venda", "Impostos", "Outros Custos"))
        print("+-------------------------------------------------+")
        print("| R$ {:<12.2f} | R$ {:<10.2f} | R$ {:<10.2f} |".format(preco_venda, imposto, outros_custos))
        print("+-------------------------------------------------+")
        print("| {:<47} |".format("            Margem de Lucro"))
        print("+-------------------------------------------------+")
        print("| {:<45.1f}%  |".format(margem))
        print("+-------------------------------------------------+")
        print("| {:<47} |".format("           Classificação do Lucro"))
        print("+-------------------------------------------------+")
        print("| {:<56} |".format(classificacao_formatada))
        print("+-------------------------------------------------+")

        # Inserir os resultados no banco de dados
        inserir_resultados(id_prato, preco_venda, custo_fixo_prato, imposto, margem)

        # Sai do loop após encontrar o item desejado
        break

# Se o item não foi encontrado, exibe uma mensagem
if not item_encontrado:
    print("O ID do prato fornecido não foi encontrado.")