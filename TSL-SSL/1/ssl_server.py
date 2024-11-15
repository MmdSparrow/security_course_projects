import socket
import ssl

def start_ssl_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="../../server_cert.pem", keyfile="../../server_key.pem")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8585))
    server_socket.listen(1)
    print("Server listening on port 8585...")

    while True:
        with context.wrap_socket(server_socket, server_side=True) as secure_socket:
            conn, addr = secure_socket.accept()
            print("Connection from:", addr)
            data = conn.recv(1024).decode()
            print("Received:", data)
            conn.sendall(b"Hello from the secure server!")
    conn.close()

start_ssl_server()