import mysql.connector
from config import Config


def get_connection():
    """
    Devuelve una conexión MySQL.

    - Local (MYSQL_SSL=false): conexión simple sin SSL.
    - Aiven / Render (MYSQL_SSL=true): conexión con SSL requerido.
      Aiven acepta SSL sin necesitar el certificado CA cuando se usa
      ssl_disabled=False + ssl_verify_cert=False, lo que funciona
      con mysql-connector-python sin archivos extra.
    """
    params = dict(
        host     = Config.MYSQL_HOST,
        port     = Config.MYSQL_PORT,
        user     = Config.MYSQL_USER,
        password = Config.MYSQL_PASSWORD,
        database = Config.MYSQL_DB,
        charset  = "utf8mb4",
        connection_timeout = 10,
    )

    if Config.MYSQL_SSL:
        params["ssl_disabled"]     = False
        params["ssl_verify_cert"]  = False
        params["ssl_verify_identity"] = False

    return mysql.connector.connect(**params)


# Alias para compatibilidad con código anterior que usaba obtener_conexion()
def obtener_conexion():
    return get_connection()
