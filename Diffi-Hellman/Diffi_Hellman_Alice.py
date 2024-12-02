import socket
import random
from time import sleep
from utils import mod_exp

q = 137
alpha = 134

print(f"Hi Alice! \u03B1={alpha} and q={q} :).")
print("I'm trying to create a random number for you (as your private key)!")
sleep(2)
X_Alice= random.randint(1, q-1)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

conn, addr = server.accept()

Y_Alice = mod_exp(alpha, X_Alice, q)
print("I will send your public server value Y to Bob.")

conn.send(str(Y_Alice).encode())

Y_Bob = int(conn.recv(1024).decode())
sleep(1)
print(f"I send your Y to Bob and he sends this for you: Y_Bob= {Y_Bob}")

shared_secret = mod_exp(Y_Bob, X_Alice, q)
print(f"Your shared secret: {shared_secret}")

server.close()
