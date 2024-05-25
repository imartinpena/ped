import os, time

# Nombre personalizado para la FIFO en función del grupo de prácticas, por ejemplo, grupo1
fifo_name = '/tmp/grupo1_cliserv_fifo'

# Crear la FIFO si no existe
if not os.path.exists(fifo_name):
    os.mkfifo(fifo_name)

# Servidor escribiendo en la FIFO
while True:
    with open(fifo_name, 'w') as fifo:
        tiempo = time.ctime(time.time())  # Obtener el tiempo actual
        fifo.write(tiempo + '\n')  # Escribir el tiempo en la FIFO
        print(f"Servidor (serv3) ha escrito: {tiempo}")
    time.sleep(1)  # Esperar un segundo antes de la próxima escritura
