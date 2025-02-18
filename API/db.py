import mysql.connector
from mysql.connector import pooling

# Configura la connexió a MariaDB
db_config = {
    'host': 'mariadb',
    'user': 'david',
    'password': '1357924680',
    'database': 'finances',  # Asegúrate de que la base de datos es la correcta
    'collation': 'utf8mb4_general_ci'
}

# Pool de connexions
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_db_connection():
    return db_pool.get_connection()

