import os, sys

# Nombre personalizado para la FIFO en función del grupo de prácticas
fifo_name = '/tmp/grupo1_cliserv_fifo'

# Comprobar si la FIFO existe
if not os.path.exists(fifo_name):
    print(f"No existe la FIFO {fifo_name}. Por favor, ejecute primero el servidor.")
    sys.exit(1)

# Cliente leyendo de la FIFO
with open(fifo_name, 'r') as fifo:
    while True:
        data = fifo.readline().strip()  # Leer datos de la FIFO
        if data:
            print(f"Cliente (cli3) ha recibido: {data}")
        else:
            break  # Salir del bucle si no hay más datos
