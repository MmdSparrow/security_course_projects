# import socket
# import ssl

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile='server.pem', keyfile='server.key')

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 4433))
# server_socket.listen(1)

# with context.wrap_socket(server_socket, server_side=True) as tls_socket:
#     print("Server is listening...")
#     conn, addr = tls_socket.accept()
#     print(f"Connection from {addr}")
#     conn.send(b"Hello over TLS")
#     conn.close()

