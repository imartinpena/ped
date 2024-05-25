import socket

# Crear un socket TCP
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Solicitar dirección y puerto del servidor
dir_socket = input("Introduzca la dirección del servidor (predeterminado: 127.0.0.1): ")
puerto = input("Introduzca el puerto del servidor (predeterminado: 65535): ")

# Usar valores predeterminados si no se ingresan datos
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '65535'

# Intentar conectar al servidor
try:
    sc.connect((dir_socket, int(puerto)))  # El cliente se conecta al socket
except Exception as e:
    print(f"Error al conectar: {e}")
    exit()

# Enviar solicitud para obtener la hora
mensaje = "¿Qué hora es?"
sc.send(mensaje.encode('utf8'))

# Mostrar la respuesta del servidor
respuesta = sc.recv(1024).decode('utf8')
print(f"Hora recibida del servidor: {respuesta}")

sc.close()