import socket
from datetime import datetime
from controller import Minefield
import ast
import subprocess

ENCODE = "UTF-8"
HOST = '127.0.0.1'   
PORT = 5000          
MAX_BYTES = 65535    


def client():
    sizeField = int(input("Informe o tamanho total:"))
    numberBobm = int(input("Informe quantidade de bombas:"))
    
    cm = Minefield(sizeField)
    cm.dict['column'] = numberBobm
    cm.dict['line'] = sizeField
    
    request = cm.dict
    request = str(request)
    request = request.encode(ENCODE)				    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    dest = (HOST, PORT)                                      
    sock.sendto(request, dest)                                 
    answer, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados

    answer = answer.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
    answer = ast.literal_eval(answer)

    if(answer['altered'] == True):
        cm.updateDict(answer)
        cm.showCleanField()
        answer['msg']
        print('Falta decobrir', answer['freeAreas'], 'áreas')

    sock.close()
    
    while True:
        cm.dict['played'] = cm.dict['played'] + 1
        line = int(input("Informe a linha:"))
        column = int(input("Informe a coluna:"))

        cm.dict['line'] = line
        cm.dict['column'] = column
        cm.dict['played'] += cm.dict['played']

        request = cm.dict
        request = str(request)
        request = request.encode(ENCODE)				   
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        dest = (HOST, PORT)                                     
        sock.sendto(request, dest)                                

        subprocess.call('cls', shell=True)
    
        answer, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
        answer = answer.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
        answer = ast.literal_eval(answer)

        if(answer['altered'] == True):
            cm.updateDict(answer)
            cm.showCleanField()
            print(answer['msg'])
            print('Falta ainda descobrir', answer['freeAreas'], 'áreas')
        else:
            cm.showCleanField()
            print(answer['msg'])
            print('Falta ainda descobrir', answer['freeAreas'], 'áreas')

        if(answer['controlPlay'] == 2):
            print('/n')
            print('/n')
            print('/n')
            A = int(input('Digite 1 para jogar novamente'))
        sock.close()
    client()        

client()


    
        

