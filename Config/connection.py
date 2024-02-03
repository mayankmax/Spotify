import psycopg2
def create_connection(host, database, port, user, password):
    conn = psycopg2.connect(
        host=host,
        database=database,
        port=port,
        user=user,
        password=password
    )
    return conn