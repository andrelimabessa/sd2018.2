import serverController
import ast
import subprocess
import socket
import threading
from datetime import datetime
import zmq
import sys

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5001            
HOST = ''              
players = []

context = zmq.Context()                                         
socket = context.socket(zmq.REP)                                
socket.connect("tcp://localhost:%s" % PORT)                     

def server_thread_oo():

    while True:

        data = socket.recv()                                    
        tratador = ThreadTratador(data)                         
        tratador.tratar_conexao(data)                           
                                                                


class ThreadTratador(threading.Thread):

    def __init__(self, data):                                   
        threading.Thread.__init__(self)
        self.data = data

    def tratar_conexao(self, data):
        data = data.decode(ENCODE)                                             
        data = str(data)
        data = ast.literal_eval(data)
        
        if (data['played'] == 0):                                              
            
            sizeField = data['line']                                           
            numberBomb = data['column']
            cm = serverController.MineField(sizeField, numberBomb)           
            players.append(cm)                                                 
            cm.dict = self.identificator(cm.dict)                              
            print(cm.dict.keys())
            print(cm.dict.values())
            cm.showCleanField()

        else:
            cm = players[data['id']]                                           
            cm.played(data['line'], data['column'])                            

        cm.showMineField()                                                     
        
        #Envia resposta 
        answer = str(cm.dict)                                                  
        answer = answer.encode(ENCODE)                                         
        socket.send(answer)                                                    

    def identification(self, dict):
        dict['id'] = len(players) - 1                                          
        return dict

if __name__ == "__main__":
    server_thread_oo()