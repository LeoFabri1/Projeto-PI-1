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

def log_compra(connection, celular, preco_prato, pgto, nome_prato, endereco):
    try:
        connection = conectar_bd()

        with connection.cursor() as cursor:
            query = 'INSERT INTO pagamentos (id_pagamento, celular_cliente, data_pagamento, valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega) VALUES (seq_id_pag.NEXTVAL, :1, SYSDATE, :2, :3, :4, :5)'
            cursor.execute(query, (celular, preco_prato, pgto, nome_prato, endereco))
            connection.commit()
            print("Log de compra registrado com sucesso.")
    except Exception as error:
        print(f"Ocorreu um erro ao registrar o log de compra: {error}")

def print_logs_auditoria():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT log_id, tipo_user, id_user, acao, 
                       TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                FROM log_auditoria 
                ORDER BY log_id DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()

            # Imprimir os registros
            for linha in linhas:
                id_pagamento, tipo_user, id_user, acao, timestamp = linha
                print(f"Log ID: {id_pagamento}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")

    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de auditoria: {error}")
    finally:
        connection.close()

def print_logs_acesso():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT id_pagamento, tipo_user, id_user, email, acao, 
                       TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp 
                FROM log_acesso 
                ORDER BY timestamp DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()

            # Imprimir os registros
            for linha in linhas:
                id_pagamento, tipo_user, id_user, email, acao, timestamp = linha
                print(f"Log ID: {id_pagamento}, \nTipo de Usuário: {tipo_user}, \nID do Usuário: {id_user}, \nEmail: {email}, \nAção: {acao}, \nAno-Mês-Dia - Hora:Minuto:Segundo: {timestamp}\n")

    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de acesso: {error}")
    finally:
        connection.close()

def print_logs_compras():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            query = '''SELECT 
                    id_pagamento, 
                    celular_cliente, 
                    TO_CHAR(data_pagamento, 'YYYY-MM-DD') AS formatted_date, 
                    valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega 
                FROM pagamentos
                ORDER BY id_pagamento DESC'''
            cursor.execute(query)
            linhas = cursor.fetchall()

            for linha in linhas:
                id_pagamento, celular_cliente, formatted_date, valor_pagamento, tipo_pagamento, prato_vendido, endereco_entrega = linha
                print(f"ID da Compra: {id_pagamento}, \nCelular do Cliente: {celular_cliente}, \nData: {formatted_date}, \nValor do Pagamento: {valor_pagamento}, \nTipo de Pagamento: {tipo_pagamento}, \nPrato Vendido: {prato_vendido}, \nEndereço de Entrega: {endereco_entrega}\n")

    except Exception as error:
        print(f"Ocorreu um erro ao recuperar os logs de compras: {error}")
    finally:
        connection.close()