import socket
import datetime

# Configuración de la dirección IP y el puerto
DIR_SERV = "127.0.0.1"
PUERTO_SERV = 5556

# Crear el socket UDP del servidor
socket_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
socket_serv.bind((DIR_SERV, PUERTO_SERV))

print(f"Servidor de fecha y hora activo en {DIR_SERV}:{PUERTO_SERV}")

while True:
    # Recibir solicitud del cliente
    datos, dir_cliente = socket_serv.recvfrom(1024)
    print(f"Solicitud recibida desde {dir_cliente}")

    # Obtener fecha y hora actuales
    fecha_hora = datetime.datetime.now()
    fecha_hora_str = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

    # Enviar la fecha y hora al cliente
    socket_serv.sendto(fecha_hora_str.encode("utf8"), dir_cliente)
