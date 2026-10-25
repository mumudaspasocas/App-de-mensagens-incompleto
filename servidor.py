import socket 
import time 
import threading

servidor = socket.socket()
servidor.bind(("localhost", 5000))

servidor.listen()

print("esperando o primeiro six seven")

cliente, endereço = servidor.accept()

print("primeiro conectado six seven")


print("esperando o segundo six seven")

cliente2, endereço2 = servidor.accept()

print("segundo conectado six seven")

def cliente2aa():
    while True:
        dados = cliente2.recv(1024)

        cliente.send(dados)

thread = threading.Thread(target=cliente2aa)

thread.start()

while True:
    dados = cliente.recv(1024)

    cliente2.send(dados)

