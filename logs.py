from BancodeDados.banco_de_dados import conectar_bd

def log_auditoria(connection, tipo_user, id_user, acao):
    try:
        connection=conectar_bd()
        with connection.cursor() as cursor:
            # Inserir o log de auditoria
            query = 'INSERT INTO log_auditoria (tipo_user, id_user, acao, timestamp) VALUES (:1, :2, :3, SYSTIMESTAMP)'
            cursor.execute(query, (tipo_user, id_user, acao))
            # Confirmar a transação
            connection.commit()
        
        print("Log de auditoria registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de auditoria: {error}")

def log_accesso(connection, tipo_user, id_user, email, acao):
    try:
        connection=conectar_bd()
        with connection.cursor() as cursor:
            query = 'INSERT INTO log_acesso (tipo_user, id_user, email, acao, timestamp) VALUES (:1, :2, :3, :4, SYSTIMESTAMP)'
            cursor.execute(query, (tipo_user, id_user, email, acao))
            # Confirmar a transação
            connection.commit()

            print("Log de acesso registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de acesso: {error}")