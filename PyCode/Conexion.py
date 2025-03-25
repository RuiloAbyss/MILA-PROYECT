import pyodbc

# Valores fijos de conexión
#ServidorIP = '192.168.1.72'  # Dirección IP fija del servidor
Servidor = r"ABISAI-MNKS15\RUIZLOOP"  # Nombre del servidor
BaseDatos = 'MilaProyect'  # Nombre de la base de datos
Puerto = 3883  # Puerto fijo

def conectarse(usuario ="", contrasena=""):
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={Servidor},{Puerto};DATABASE={BaseDatos};UID={usuario};PWD={contrasena}'
    
    try:
        # Establecer conexión
        connection = pyodbc.connect(connection_string)
        print("Conexión exitosa al servidor remoto")
        return connection
    except Exception as e:
        error_message = str(e)
    if "Login failed" in error_message:
        print("Error: Credenciales incorrectas")
    elif "Server does not exist" in error_message:
        print("Error: El servidor remoto no se encuentra")
    elif "timeout" in error_message:
        print("Error: Tiempo de espera agotado, verifica el puerto")
    else:
        print("Error desconocido:", error_message)


# Ejemplo de uso
'''
conexion = conectarse(usuario, contrasena)

if conexion:
    # Realiza consultas
    cursor = conexion.cursor()
    cursor.execute("SELECT TOP 10 * FROM ejemplo_tabla")  # Cambia por tu consulta SQL
    for fila in cursor:
        print(fila)
    
    # Cierra la conexión
    cursor.close()
    conexion.close()
'''