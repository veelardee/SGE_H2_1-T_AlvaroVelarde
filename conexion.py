
import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """Establece una conexión con la base de datos MySQL y la devuelve."""
    try:
        connection = mysql.connector.connect(
            host="localhost",       
            user="root",     
            password="campusfp",  
            database="encuestas",
            auth_plugin='mysql_native_password' 

        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None





