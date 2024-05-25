import os
import sys

fifo_path = '/tmp/serv3_fifo'

# Verificar que el FIFO existe
if not os.path.exists(fifo_path):
    print(f"El FIFO {fifo_path} no existe. Inicie primero el servidor.")
    sys.exit(1)

# Enviar solicitud de archivo al servidor
file_path = sys.argv[1] if len(sys.argv) > 1 else input("Ingrese la ruta del archivo: ")
with open(fifo_path, 'w') as fifo:
    fifo.write(file_path)

# Esperar y leer respuesta del servidor
with open(fifo_path, 'r') as fifo:
    content = fifo.read()
    print(f"Contenido del archivo '{file_path}':\n{content}")