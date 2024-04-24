import oracledb
import os

# Conectar ao banco de dados
def conectar_bd():
    connection=oracledb.connect(
        config_dir=os.path.dirname(os.path.realpath(__file__)),
        user="ADMIN",
        password="H7$e/ZbX@##s*.q",
        dsn="db2024_low",
        wallet_location=os.path.dirname(os.path.realpath(__file__)),
        wallet_password="H7$e/ZbX@##s*.q")
    return connection

connection = conectar_bd()