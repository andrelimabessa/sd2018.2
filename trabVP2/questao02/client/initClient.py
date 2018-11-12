import socket
import clientController
import ast
import subprocess
import zmq
import sys
import queue

ENCODE = "UTF-8"     
PORT = 5000          
MAX_BYTES = 65535    

def client():

    sizeField = int(input("Informe o tamanho total:"))      
    numberBobm = int(input("Informe a quantidade de bombas:"))      
    cm = clientController.CampoMinado(sizeField)                 
    cm.dict['line'] = sizeField                                 
    cm.dict['column'] = numberBobm                              
    request = cm.dict                                           
    request = str(request)                                     
    request = request.encode(ENCODE)				            
    
    context = zmq.Context()                                     
    print("Conectando com o servidor...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % PORT)                
    socket.send(request)                                        
    answer = socket.recv()
    answer = answer.decode(ENCODE)                            
    answer = ast.literal_eval(answer)                           
                                                                
    cm.dict['id'] = answer['id']                                
    print(cm.dict.values())
    cm.translateReturn(answer)                                  
    
    while True:
        
        #Jogada
        print('As linhas e colunas variam de 0 à', len(cm.cleanField)-1, '\n')     
        line = int(input("Informe a linha:"))                                      
        column = int(input("Informe a coluna:"))                                   
        cm.dict['line'] = line                                                      
        cm.dict['column'] = column                                                  

        print("Conectando com o servidor...")
        request = cm.dict                                      
        request = str(request)                                 
        request = request.encode(ENCODE)				       

        socket.send(request)                                   
        answer = socket.recv()
        subprocess.call('cls', shell=True)                          
        answer = answer.decode(ENCODE)                             
        answer = ast.literal_eval(answer)                           
                                                                    

        cm.translateReturn(answer)                                  

if __name__ == '__main__':
    client()


    
        

