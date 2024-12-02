import socket
import random
from time import sleep
from utils import mod_exp

q = 137
alpha = 134

print(f"Hi Bob! \u03B1={alpha} and q={q} :).")
print("I'm trying to create a random number for you (as your private key)!")
sleep(2)
X_Bob= random.randint(1, q-1)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

Y_Bob = mod_exp(alpha, X_Bob, q)
print("I will send your public server value Y to Alice.")

Y_Alice = int(client.recv(1024).decode())
sleep(1)
print(f"I send your Y to Alice and she sends this for you: Y_Alice= {Y_Alice}")

client.send(str(Y_Bob).encode())

shared_secret = mod_exp(Y_Alice, X_Bob, q)
print(f"Your shared secret: {shared_secret}")

client.close()
