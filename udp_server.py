import socket
from datetime import datetime
import controle
import json

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor



def server():

    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:

        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        print(data)
        
        text = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        text2 = list(text)
        jogada = []
        jogada.append(int(text2[1]))
        jogada.append(int(text2[4]))
        jogada.append(int(text2[7]))
        print(jogada)

        cm = controle.Campo(jogada[0], jogada[0], jogada[1])
        cm.mostrarCampo(cm.campoMinado)
        data = json.dumps(cm)
        print(data)

        #print(address, jogada)

        #Envia resposta
        text = "Total de dados recebidos: " + str(len(data)) 
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

server()