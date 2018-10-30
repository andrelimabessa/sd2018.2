import socket
from  campo_minado_negocio import CampoMinado
from datetime import datetime
from ast import literal_eval

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor

def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    objeto = CampoMinado()

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        print(address, text)

        #Tratamento Início
        text = tratar_mensagem(objeto, text)
        #Tratamento Fim

        #Envia resposta
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

def tratar_mensagem(objeto, text):
    msg = literal_eval(text)

    if msg["acao"] == "criar_jogo":
        rsp = objeto.criar_novo_jogo(int(msg["linha"]), int(msg["coluna"]))
        return str(rsp)

server()