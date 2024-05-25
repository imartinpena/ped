import socket, datetime

# Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Configurar dirección y puerto del servidor
dir_socket = input("Introduzca la dirección del servidor (predeterminado: 127.0.0.1): ")
puerto = input("Introduzca el puerto del servidor (predeterminado: 65535): ")

# Usar valores predeterminados si no se ingresan datos
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '65535'

# Enlazar el socket
sock.bind((dir_socket, int(puerto)))

# Escuchar conexiones
sock.listen(5)
print(f"Servidor escuchando en {dir_socket}:{puerto}")

while True:
    # Aceptar conexión entrante
    conn, addr = sock.accept()
    print(f"Conexión aceptada desde {addr}")

    # Recibir la solicitud del cliente
    datos = conn.recv(1024).decode('utf8')
    if datos == "¿Qué hora es?":
        # Obtener la fecha y hora actual
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.send(fecha_hora.encode('utf8'))
    else:
        conn.send("Solicitud no reconocida".encode('utf8'))

    # Cerrar la conexión con el cliente
    conn.close()
    print(f"Conexión cerrada con {addr}")
