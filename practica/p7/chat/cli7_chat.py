import socket
import threading
import sys

# Configuración del cliente
host = input("Dirección del servidor (predeterminado: 127.0.0.1): ") or "127.0.0.1"
port = int(input("Puerto del servidor (predeterminado: 65534): ") or 65534)
usuario = input("Nombre de usuario: ")

# Creación del socket del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Identificación del cliente
client.send(usuario.encode("utf-8"))
respuesta = client.recv(1024).decode("utf-8")
print(respuesta)
if respuesta.startswith("ERROR"):
    sys.exit()

# Función para escuchar mensajes entrantes
def escuchar_mensajes():
    while True:
        try:
            mensaje = client.recv(1024).decode("utf-8")
            if not mensaje:
                break
            print(mensaje)
        except Exception as e:
            print(f"Error: {str(e)}")
            break

# Hilo para recibir mensajes
thread = threading.Thread(target=escuchar_mensajes)
thread.start()

# Bucle para enviar mensajes
while True:
    mensaje = input(f"{usuario} > ")
    if mensaje:
        client.send(mensaje.encode("utf-8"))
