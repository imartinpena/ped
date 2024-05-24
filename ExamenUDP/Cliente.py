import socket, sys
from cliserv import Cliserv

# creo socket
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 

dir_socket = input("Introduce la dirección del servidor (por defecto '127.0.0.1'): ") or '127.0.0.1'
puerto = input("Introduce el puerto del servidor (por defecto 16013): ") or '16013'
if not dir_socket:
    dir_socket = 'localhost'
if not puerto:
    puerto = '16013'

devuelve = Cliserv()
peticion = devuelve.pide()
sc.sendto(peticion.encode('utf8'), (dir_socket, int(puerto)))

data, dir = sc.recvfrom(1024)
sys.stdout.write(data.decode('utf8').strip()) 
print("\n")
sc.close()
