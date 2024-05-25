import socket

# Configuración del servidor
DIR_SERV = "127.0.0.1"
PUERTO_SERV = 5556

# Crear el socket UDP del cliente
socket_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# Enviar solicitud para obtener la fecha y hora actuales
mensaje = "¿Qué hora es?"
socket_cli.sendto(mensaje.encode("utf8"), (DIR_SERV, PUERTO_SERV))

# Recibir la respuesta del servidor
respuesta, _ = socket_cli.recvfrom(1024)
print("Fecha y hora actuales:", respuesta.decode("utf8"))

socket_cli.close()
