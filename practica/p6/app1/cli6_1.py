import socket

# Crear un socket TCP
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Solicitar dirección y puerto del servidor
dir_socket = input("Introduzca la dirección del servidor (predeterminado: 127.0.0.1): ")
puerto = input("Introduzca el puerto del servidor (predeterminado: 8000): ")

# Usar valores predeterminados si no se ingresan datos
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '8000'

# Intentar conectar al servidor
try:
    sc.connect((dir_socket, int(puerto)))  # El cliente se conecta al socket
except Exception as e:
    print(f"Error al conectar: {e}")
    exit()

# Solicitar el path del archivo deseado
path = input("Introduzca el path del archivo que quiere leer: ")
sc.send(path.encode('utf8'))

# Mostrar el contenido recibido
print(f"Path enviado. El contenido del fichero en {path} es:")
while True:
    data = sc.recv(1024)
    if not data:
        break
    print(data.decode('utf8'))
sc.close()
