import socket
import threading

# Configuración del servidor
host = "127.0.0.1"
port = 65533
articulos = {}
clientes = {}
usuarios = set()

# Crear el socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"Servidor de noticias escuchando en {host}:{port}")

# Función para manejar cada cliente
def manejar_cliente(cliente_socket):
    try:
        usuario = cliente_socket.recv(1024).decode("utf-8")
        if usuario in usuarios:
            cliente_socket.send("ERROR: Usuario en uso.".encode("utf-8"))
            cliente_socket.close()
            return
        usuarios.add(usuario)
        clientes[cliente_socket] = usuario
        cliente_socket.send("Conectado al servidor de noticias.".encode("utf-8"))

        while True:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            if mensaje.startswith("PUBLICAR"):
                asunto, contenido = mensaje.split(": ", 1)
                articulos[asunto] = contenido
                print(f"Nuevo artículo: {asunto} - {contenido}")
                for cs in clientes:
                    if cs != cliente_socket:
                        cs.send(f"{usuario} publicó {asunto}".encode("utf-8"))
            elif mensaje.startswith("LEER"):
                for asunto, contenido in articulos.items():
                    cliente_socket.send(f"{asunto}: {contenido}".encode("utf-8"))
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        usuarios.remove(clientes[cliente_socket])
        del clientes[cliente_socket]
        cliente_socket.close()

# Aceptar nuevas conexiones
while True:
    cliente_socket, direccion_cliente = server.accept()
    print(f"Conexión aceptada desde {direccion_cliente[0]}:{direccion_cliente[1]}")
    thread = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
    thread.start()
