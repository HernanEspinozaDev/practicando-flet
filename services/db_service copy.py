import psycopg2

def connect_db():
    return psycopg2.connect(
        host="tu-rds-host",
        database="nombre-de-tu-bd",
        user="tu-usuario",
        password="tu-password",
        port="5432"  # Puerto por defecto
    )