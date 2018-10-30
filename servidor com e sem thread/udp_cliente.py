import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'  
PORT = 5000         
MAX_BYTES = 65535   

def client():

    print("converver dados")
    text = input("Digite algum texto:\n")   		  
    print("converver dados")
    data = text.encode(ENCODE)				   
    print("converver dados")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    dest = (HOST, PORT)                                   
    sock.sendto(data, dest)                                

    print(sock.getsockname())				   
    data, address = sock.recvfrom(MAX_BYTES)              
    text = data.decode(ENCODE)                             
    print(address, text)                                   
