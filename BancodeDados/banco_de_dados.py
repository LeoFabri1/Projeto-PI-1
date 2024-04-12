import oracledb

# Conectar ao banco de dados
def conectar_bd():
    connection=oracledb.connect(
        config_dir=r"C:\OracleCloud\Wallet\Wallet_ProjetoIntegrador1.zip",
        user="admin",
        password="H7$e/ZbX@##s*.q",
        dsn="db2024_low",
        wallet_location=r"C:\OracleCloud\Wallet\Wallet_ProjetoIntegrador1.zip",
        wallet_password="H7$e/ZbX@##s*.q")
    return connection

connection = conectar_bd()