import socket
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python cli4_1.py <ruta_del_archivo>")
        sys.exit(1)

    file_path = sys.argv[1]
    server_address = '/tmp/cli4_serv4_app1_socket'  # Ruta del socket UDS

    # Creación del socket UDS
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(server_address)  # Conexión al servidor
        print("Conectado al servidor.")
        sock.sendall(file_path.encode())  # Envío del path del archivo

        # Recibir y mostrar respuesta
        response = sock.recv(1024)
        print("Contenido recibido:")
        print(response.decode())
    finally:
        sock.close()

if __name__ == "__main__":
    main()
