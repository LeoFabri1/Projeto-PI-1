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

def print_logs_auditoria():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT log_id, tipo_user, id_user, acao, 
                       TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                FROM log_auditoria 
                ORDER BY timestamp DESC'''
            cursor.execute(query)
            rows = cursor.fetchall()

            # Imprimir os registros
            for row in rows:
                log_id, tipo_user, id_user, acao, timestamp = row
                print(f"Log ID: {log_id}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")

    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de auditoria: {error}")
    finally:
        connection.close()

def print_logs_acesso():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT log_id, tipo_user, id_user, email, acao, 
                       TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                FROM log_acesso 
                ORDER BY timestamp DESC'''
            cursor.execute(query)
            rows = cursor.fetchall()

            # Imprimir os registros
            for row in rows:
                log_id, tipo_user, id_user, email, acao, timestamp = row
                print(f"Log ID: {log_id}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nEmail: {email}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")

    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de acesso: {error}")
    finally:
        connection.close()