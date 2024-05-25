import os
import sys

def serv2(read_fd):
    read_pipe = os.fdopen(read_fd, 'r')
    while True:
        file_path = read_pipe.readline().strip()
        if not file_path:
            break
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "Archivo no encontrado."
        print(f"Contenido del archivo {file_path}:\n{content}")
    read_pipe.close()

def cli2(write_fd, file_path):
    write_pipe = os.fdopen(write_fd, 'w')
    write_pipe.write(file_path + '\n')
    write_pipe.flush()
    write_pipe.close()

def main(file_path):
    read_fd, write_fd = os.pipe()
    pid = os.fork()

    if pid > 0:  # Proceso padre (serv2)
        os.close(write_fd)  # Cierra el extremo de escritura no utilizado en el padre
        serv2(read_fd)
    else:  # Proceso hijo (cli2)
        os.close(read_fd)  # Cierra el extremo de lectura no utilizado en el hijo
        cli2(write_fd, file_path)
        os._exit(0)  # Termina el proceso hijo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("SINTAXIS: python3 cliserv2.py <nombre_archivo>")
        sys.exit(1)
    main(sys.argv[1])

