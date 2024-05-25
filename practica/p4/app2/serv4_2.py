import socket
import os
import time

def main():
    server_address = '/tmp/cli4_serv4_app2_socket'

    # Asegurarse que el socket no exista ya
    try:
        os.unlink(server_address)
    except OSError:
        if os.path.exists(server_address):
            raise

    # Creación del socket y configuración
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)  # Solo un cliente en espera (ajustable)

    print("Servidor de fecha y hora esperando conexiones en", server_address)
    while True:
        connection, client_address = sock.accept()
        try:
            print("Conexión aceptada", client_address)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            connection.sendall(current_time.encode())  # Envío de la fecha y hora
        finally:
            connection.close()

if __name__ == "__main__":
    main()
