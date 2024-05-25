import socket
import threading
import sys

# Configuración del cliente
host = input("Dirección del servidor (predeterminado: 127.0.0.1): ") or "127.0.0.1"
port = int(input("Puerto del servidor (predeterminado: 65533): ") or 65533)
usuario = input("Nombre de usuario: ")

# Crear el socket del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Identificación del cliente
client.send(usuario.encode("utf-8"))
respuesta = client.recv(1024).decode("utf-8")
print(respuesta)
if respuesta.startswith("ERROR"):
    sys.exit()

# Función para escuchar noticias
def escuchar_noticias():
    while True:
        try:
            noticia = client.recv(1024).decode("utf-8")
            if not noticia:
                break
            print(noticia)
        except Exception as e:
            print(f"Error: {str(e)}")
            break

# Hilo para recibir noticias
thread = threading.Thread(target=escuchar_noticias)
thread.start()

# Bucle para enviar mensajes (publicar o leer)
while True:
    comando = input("Escriba 'PUBLICAR' para añadir una noticia o 'LEER' para ver las existentes: ").upper()
    if comando == "PUBLICAR":
        asunto = input("Asunto: ")
        contenido = input("Contenido: ")
        client.send(f"PUBLICAR: {asunto}: {contenido}".encode("utf-8"))
    elif comando == "LEER":
        client.send("LEER".encode("utf-8"))
