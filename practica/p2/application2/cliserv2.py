import os
import sys
from datetime import datetime

def serv2(read_pipe):
    while True:
        signal = read_pipe.readline().strip()
        if not signal:
            break
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Servidor (serv2) envía la fecha y hora actual: {current_time}")

def cli2(write_pipe):
    write_pipe.write("solicitud\n")
    write_pipe.flush()

def main():
    read_fd, write_fd = os.pipe()
    pid = os.fork()

    if pid > 0:  # Proceso padre (serv2)
        os.close(write_fd)
        read_pipe = os.fdopen(read_fd, 'r')
        serv2(read_pipe)
    else:  # Proceso hijo (cli2)
        os.close(read_fd)
        write_pipe = os.fdopen(write_fd, 'w')
        cli2(write_pipe)
        sys.exit(0)  # Asegurar que el proceso hijo termina después de enviar la solicitud

if __name__ == "__main__":
    main()
