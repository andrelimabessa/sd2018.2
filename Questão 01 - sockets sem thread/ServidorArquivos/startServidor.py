import servidorControle
import socket
from datetime import datetime
import ast
import subprocess

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000           
HOST = ''     	       



def server():

    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:

        data, address = sock.recvfrom(MAX_BYTES) 
        data = data.decode(ENCODE)               
        data = str(data)
        data = ast.literal_eval(data)
        print(data.keys())
        print(data.values())
        if (data['played'] == 0):
            sizeField = data['line']
            numberBomb = data['column']
            cm = servidorControle.CampoMinado(sizeField, numberBomb)
            print(cm.dict.keys())
            cm.showCleanField()
            cm.showMineField()
        else:
            cm.played(data['line'], data['column'])                

        cm.showMineField()
        answer = str(cm.dict)
    
        answer = answer.encode(ENCODE) 
        sock.sendto(answer, address) 
server()