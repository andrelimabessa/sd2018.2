# coding: utf-8
import socket
import threading
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000  
HOST = ''   


""" Forma Orientado a objeto """
def server_thread_oo():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
 
        tratador = ThreadTratador(sock, data, address)
        tratador.start()

""" Forma Procedural """
def server_thread_procedural():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        t = threading.Thread(target=tratar_conexao, args=tuple([sock, data, address]))
        t.start()

def tratar_conexao(sock, data, address):
    text = data.decode(ENCODE)
    print(text)
    text = "Quantidade de bytes enviados: " + str(len(data))
    data = text.encode(ENCODE)
    sock.sendto(data, address)

class ThreadTratador(threading.Thread):

    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.sock = a
        self.data = b
        self.address = c

    def run(self):

        tratar_conexao(self.sock, self.data, self.address)


