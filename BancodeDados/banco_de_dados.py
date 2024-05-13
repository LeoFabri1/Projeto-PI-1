import oracledb
import os

# Conectar ao banco de dados
def conectar_bd():
    try:
        connection=oracledb.connect(
            config_dir=os.path.dirname(os.path.realpath(__file__)),
            user="ADMIN",
            password="H7$e/ZbX@##s*.q",
            dsn="ProjetoIntegrador1_low",
            wallet_location=os.path.dirname(os.path.realpath(__file__)),
            wallet_password="H7$e/ZbX@##s*.q")
        return connection
    except Exception as error:
        print("Erro ao conectar no banco: ", error)

connection = conectar_bd()