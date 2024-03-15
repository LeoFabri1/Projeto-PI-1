import oracledb

# Conectar ao banco de dados
def conectar_bd():
    connection = oracledb.connect(user="BD150224513", password="Opxuf5", host="172.16.12.14", port="1521")
    return connection

connection = conectar_bd()