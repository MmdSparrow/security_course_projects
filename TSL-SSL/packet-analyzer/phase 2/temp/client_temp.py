# import socket
# import ssl

# context = ssl.create_default_context()
# with socket.create_connection(('localhost', 4433)) as sock:
#     with context.wrap_socket(sock, server_hostname="localhost") as tls_socket:
#         print(tls_socket.recv(1024).decode())
