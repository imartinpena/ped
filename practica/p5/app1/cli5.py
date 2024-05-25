import socket

# Configuración del servidor
DIR_SERV = "127.0.0.1"
PUERTO_SERV = 5555

# Solicitar el path del archivo
path = input("Path del archivo a solicitar: ").strip()

# Crear el socket UDP del cliente
socket_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# Enviar la solicitud del archivo al servidor
socket_cli.sendto(path.encode("utf8"), (DIR_SERV, PUERTO_SERV))

# Recibir el contenido del archivo
full_msg = ""
datos = "Empieza"
while datos:
    datos, _ = socket_cli.recvfrom(1024)
    if datos:
        full_msg += datos.decode("latin-1")
    else:
        break

print("Contenido del archivo recibido:\n", full_msg)
socket_cli.close()