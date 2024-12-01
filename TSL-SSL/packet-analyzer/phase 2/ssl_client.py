import socket
import ssl

def start_ssl_client():
    context = ssl.create_default_context()
    context.check_hostname = False  # Bypass hostname verification for simplicity
    context.verify_mode = ssl.CERT_NONE  # Bypass certificate verification

    with socket.create_connection(('localhost', 8585)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname='localhost') as secure_socket:
            secure_socket.sendall(b"Hello from the client!")
            response = secure_socket.recv(1024)
            print("Received from server:", response.decode())

start_ssl_client()
