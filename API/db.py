import mysql.connector
from mysql.connector import pooling

# Configura la connexió a MariaDB
db_config = {
    'host': 'mariadb',
    'user': 'david',
    'password': '1357924680',
    'database': 'reserves',
    'collation': 'utf8mb4_general_ci'
}

# Pool de connexions
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_db_connection():
    return db_pool.get_connection()

def insert_ingreso(titol, descripcio, quantitat, data):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO ingresos (titol, descripcio, quantitat, data) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (titol, descripcio, quantitat, data))
        connection.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()

def get_ingreso(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM ingresos WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()

def update_ingreso(id, titol, descripcio, quantitat, data):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "UPDATE ingresos SET titol = %s, descripcio = %s, quantitat = %s, data = %s WHERE id = %s"
        cursor.execute(query, (titol, descripcio, quantitat, data, id))
        connection.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        connection.close()

def delete_ingreso(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM ingresos WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        connection.close()

def list_ingresos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM ingresos"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()