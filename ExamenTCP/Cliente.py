import socket
import sys
from cliserv import Cliserv

def obtener_direccion_y_puerto():
    dir_socket = input("Introduce la dirección del servidor (por defecto '127.0.0.1'): ") or '127.0.0.1'
    puerto = input("Introduce el puerto del servidor (por defecto 16013): ") or '16013'
    if not dir_socket:
        dir_socket = 'localhost'
    if not puerto:
        puerto = '16013'
    return dir_socket, int(puerto)

def main():
    dir_socket, puerto = obtener_direccion_y_puerto()
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((dir_socket, puerto))

    devuelve = Cliserv()
    while True:
        peticion = devuelve.pide()
        if peticion.lower() == 'salir':
            break
        sc.sendall(peticion.encode('utf8'))

        data = sc.recv(1024).decode('utf8')
        sys.stdout.write(data.strip())
        print("\n")

    sc.close()

if __name__ == "__main__":
    main()