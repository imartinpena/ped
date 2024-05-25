import socket
import os

def main():
    server_address = '/tmp/cli4_serv4_app1_socket'

    # Asegurarse que el socket no exista ya
    try:
        os.unlink(server_address)
    except OSError:
        if os.path.exists(server_address):
            raise

    # Creación del socket y configuración
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_address)  # Vincular al archivo de socket UDS
    sock.listen(1)  # Solo un cliente en espera (este valor es ajustable)

    print("Servidor esperando conexiones en", server_address)
    while True:
        connection, client_address = sock.accept()
        try:
            print("Conexión aceptada", client_address)
            while True:
                data = connection.recv(1024)
                if data:
                    file_path = data.decode()
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                            connection.sendall(content.encode())
                    except FileNotFoundError:
                        msg = "Archivo no encontrado."
                        connection.sendall(msg.encode())
                else:
                    break
        finally:
            connection.close()

if __name__ == "__main__":
    main()
