import socket
import os

# Configuración de la dirección IP y el puerto
DIR_SERV = "127.0.0.1"
PUERTO_SERV = 5555

# Crear el socket UDP del servidor
socket_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
socket_serv.bind((DIR_SERV, PUERTO_SERV))

print(f"Servidor en funcionamiento en {DIR_SERV}:{PUERTO_SERV}")

while True:
    # Recibir la solicitud de archivo del cliente
    path, dir_cliente = socket_serv.recvfrom(1024)
    path = path.decode("utf8").strip()
    print(f"Solicitud de archivo: {path}")
    print(f"Dirección del cliente: {dir_cliente}")

    try:
        # Abrir y leer el archivo solicitado
        with open(path, "rb") as archivo:
            mensaje = "Empieza"
            while mensaje:
                mensaje = archivo.read(1024)
                socket_serv.sendto(mensaje, dir_cliente)
    except Exception as e:
        error = str(e).encode("utf8")
        socket_serv.sendto(error, dir_cliente)
