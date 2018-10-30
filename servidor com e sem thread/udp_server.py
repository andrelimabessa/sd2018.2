import socket
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000          
HOST = ''     	    

def server():
    #Abrindo na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        print(address, text)

        text = "Your data was " + str(len(data)) + " bytes long"
        data = text.encode(ENCODE)
        sock.sendto(data, address) 
    sock.close()
