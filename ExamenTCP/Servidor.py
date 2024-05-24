import socket
import os
import sys
from cliserv import Cliserv

def iniciar_servidor(direccion, puerto):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind((direccion, int(puerto)))
        ss.listen(5)
        print(f"Servidor TCP escuchando en {direccion} por el puerto {puerto}...")
        return ss
    except Exception as e:
        print(f"Error al asignar una dirección al servidor: {e}")
        sys.exit(1)

def manejar_peticion(conexion, peticion, devuelve):
    if peticion == "NO CAPICUA Y NO PALINDROMO":
        conexion.sendall(peticion.encode('utf8'))
    elif devuelve.esNatural(peticion):  # Comprueba si es un número natural
        print("El cliente ha introducido un número")
        if devuelve.esCapicua(peticion):  # Comprueba si el número es capicúa
            conexion.sendall("Si es capicua".encode('utf8'))
        else:  # Si no es capicúa
            conexion.sendall("No es capicua".encode('utf8'))
    else:  # Si no es un número natural
        if devuelve.esPalindromo(peticion):  # Comprueba si es un palíndromo
            conexion.sendall("Si es palindromo".encode('utf8'))
        else:  # Si no es palíndromo
            conexion.sendall("No es palindromo".encode('utf8'))

def servidor():
    direccion = input("Introduce la dirección del servidor (por defecto '127.0.0.1'): ") or '127.0.0.1'
    puerto = input("Introduce el puerto del servidor (por defecto 16013): ") or '16013'
    if not direccion:
        direccion = 'localhost'
    if not puerto:
        puerto = '16013'

    ss = iniciar_servidor(direccion, puerto)
    devuelve = Cliserv()

    while True:
        conexion, dirc = ss.accept()
        pid = os.fork()
        if pid:  # Proceso padre, proceso servidor.
            conexion.close()
            continue
        else:  # Proceso hijo, proceso que gestiona la solicitud
            data = conexion.recv(1024).decode('utf8')
            manejar_peticion(conexion, data, devuelve)
            conexion.close()
            print("El cliente ha cerrado conexión")
            exit()

if __name__ == "__main__":
    servidor()