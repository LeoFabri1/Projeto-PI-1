import numpy as np

desc_cripto = ""
desc_vetorfinal = []
desc_prato = []
matriz = [[], []]
matriz_chave = np.array([[2, 1], [5, 3]])
matriz_inversa = np.array([[3, -1], [-5, 2]])

dic_modulo29 = [
    {
        "Modulo29": {
            "A" : 1,
            "B" : 2,
            "C" : 3,
            "D" : 4,
            "E" : 5,
            "F" : 6,
            "G" : 7,
            "H" : 8,
            "I" : 9,
            "J" : 10,
            "K" : 11,
            "L" : 12,
            "M" : 13,
            "N" : 14,
            "O" : 15,
            "P" : 16,
            "Q" : 17,
            "R" : 18,
            "S" : 19,
            "T" : 20,
            "U" : 21,
            "V" : 22,
            "W" : 23,
            "X" : 24,
            "Y" : 25,
            "Z" : 26,
            " " : 27,
            "," : 28,
            "." : 29
        }
    }
]

def cripto(descricao):
    #fazer virar par
    if len(descricao) % 2 != 0:
        descricao += " "
    #transformar string em vetor
    desc_prato = list(descricao)
    #transforma em numero
    for i in descricao.upper():  # Converte para maiúsculas
        #adiciona de acordo com dicionario
        if i in dic_modulo29:
            desc_prato.append(dic_modulo29[i])
    #transforma em matriz
    for i in range(0, len(desc_prato), 2):
        # Adiciona o primeiro elemento do par à primeira linha
        matriz[0].append(desc_prato[i])
        # Adiciona o segundo elemento do par à segunda linha
        matriz[1].append(desc_prato[i + 1])
    #multiplicar matriz pela chave
    matriz_cripto = np.dot(np.array(matriz), np.array(matriz_chave))
    #transforma em letras
    np.mod(matriz_cripto, 29)
    #transforma em vetor
    desc_vetorfinal = matriz_cripto.flatten()
    #transforma em string
    desc_cripto = "".join(desc_vetorfinal)
    #retorna a frase criptografada para ser inserida no banco
    return desc_cripto

def descripto():
    #fazer decodificacao aqui
    print('Decodificado.')
    desc_prato_decodificado = "".join(desc_prato)#vira string
    return desc_prato_decodificado