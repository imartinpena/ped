import socket
import sys

def main():
    server_address = '/tmp/cli4_serv4_app2_socket'  # Ruta del socket UDS

    # Creación del socket UDS
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(server_address)  # Conexión al servidor
        print("Conectado al servidor de fecha y hora.")
        response = sock.recv(1024)  # Recibir respuesta
        print("Fecha y hora actual:", response.decode())
    finally:
        sock.close()

if __name__ == "__main__":
    main()
