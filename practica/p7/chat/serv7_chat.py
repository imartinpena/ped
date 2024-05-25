import socket
import threading

# Configuración del servidor
host = "127.0.0.1"  # Dirección local
port = 65534
clientes = {}
usuarios = set()

# Creación del socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"Servidor escuchando en {host}:{port}")

# Función para manejar las conexiones con cada cliente
def manejar_cliente(cliente_socket):
    try:
        # Identificación única del usuario
        usuario = cliente_socket.recv(1024).decode("utf-8")
        if usuario in usuarios:
            cliente_socket.send("ERROR: Este nombre de usuario ya está en uso.".encode("utf-8"))
            cliente_socket.close()
            return
        usuarios.add(usuario)
        clientes[cliente_socket] = usuario
        cliente_socket.send("Conectado al chat.".encode("utf-8"))

        # Bucle para recibir y reenviar mensajes
        while True:
            mensaje = cliente_socket.recv(1024)
            if not mensaje:
                break
            mensaje_str = f"{usuario}: {mensaje.decode('utf-8')}"
            print(mensaje_str)
            # Reenviar a todos los demás clientes
            for cs in clientes:
                if cs != cliente_socket:
                    cs.send(mensaje_str.encode("utf-8"))
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Manejar desconexión
        usuarios.remove(clientes[cliente_socket])
        del clientes[cliente_socket]
        cliente_socket.close()

# Aceptar nuevas conexiones
while True:
    cliente_socket, cliente_direccion = server.accept()
    print(f"Conexión aceptada desde {cliente_direccion[0]}:{cliente_direccion[1]}")
    thread = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
    thread.start()
