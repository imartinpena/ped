import socket
import os
import sys
from cliserv import Cliserv

def iniciar_servidor(direccion, puerto):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)  # Creo socket UDP
        ss.bind((direccion, int(puerto)))
        print(f"Servidor UDP escuchando en {direccion} por el puerto {puerto}...")
        return ss
    except Exception as e:
        print(f"Error al asignar una dirección al servidor: {e}")
        sys.exit(1)

def manejar_peticion(ss, peticion, dirc, devuelve):
    if peticion == "NO CAPICUA Y NO PALINDROMO":
        ss.sendto(peticion.encode('utf8'), dirc)
    elif devuelve.esNatural(peticion):  # Comprueba si es un número natural
        print("El cliente", dirc, "ha introducido un número")
        if devuelve.esCapicua(peticion):  # Comprueba si el número es capicúa
            ss.sendto("Si es capicua".encode('utf8'), dirc)
        else:  # Si no es capicúa
            ss.sendto("No es capicua".encode('utf8'), dirc)
    else:  # Si no es un número natural
        if devuelve.esPalindromo(peticion):  # Comprueba si es un palíndromo
            ss.sendto("Si es palindromo".encode('utf8'), dirc)
        else:  # Si no es palíndromo
            ss.sendto("No es palindromo".encode('utf8'), dirc)

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
        data, dirc = ss.recvfrom(1024)
        peticion = data.decode('utf8')
        pid = os.fork()
        if pid:  # Proceso padre, proceso servidor.
            continue
        else:  # Proceso hijo, proceso que gestiona la solicitud
            manejar_peticion(ss, peticion, dirc, devuelve)
            ss.close()
            print("El cliente", dirc, "ha cerrado conexión")
            exit()

if __name__ == "__main__":
    servidor()