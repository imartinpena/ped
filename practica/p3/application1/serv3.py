import os
import time

fifo_path = '/tmp/serv3_fifo'

# Crear FIFO si no existe
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

while True:
    # Esperar solicitud del cliente
    with open(fifo_path, 'r') as fifo:
        file_path = fifo.readline().strip()
        if not file_path:
            time.sleep(1)
            continue

    # Leer y enviar contenido del archivo
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except Exception as e:
        content = f"Error al leer el archivo: {str(e)}"

    with open(fifo_path, 'w') as fifo:
        fifo.write(content)
