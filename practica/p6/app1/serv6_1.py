import socket, os

# Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Configurar dirección y puerto del servidor
dir_socket = input("Introduzca la dirección del servidor (predeterminado: 127.0.0.1): ")
puerto = input("Introduzca el puerto del servidor (predeterminado: 8000): ")

# Usar valores predeterminados si no se ingresan datos
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '8000'

# Enlazar el socket
sock.bind((dir_socket, int(puerto)))

# Escuchar conexiones
sock.listen(5)
print(f"Servidor escuchando en {dir_socket}:{puerto}")

while True:
    # Aceptar conexión entrante
    conn, addr = sock.accept()
    print(f"Conexión aceptada desde {addr}")

    # Recibir el path del archivo solicitado
    path = conn.recv(1024).decode('utf8').strip()
    print(f"El cliente solicitó el archivo: {path}")

    try:
        # Leer el contenido del archivo y enviarlo al cliente
        with open(path, 'r') as f:
            for line in f:
                conn.send(line.encode('utf8'))
    except Exception as e:
        # Enviar un mensaje de error al cliente si ocurre un problema
        error_msg = f"Error: {str(e)}"
        conn.send(error_msg.encode('utf8'))

    # Cerrar la conexión con el cliente
    conn.close()
    print(f"Conexión cerrada con {addr}")
