import socket
from datetime import datetime
from ast import literal_eval

GAME_OVER = "GAME_OVER"

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def enviar_servidor(text):
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """

    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    
    #Enviando de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
    dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
    sock.sendto(data, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor
    data, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
    text = data.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
    print(text)

    #Fechando Socket
    sock.close()

    return text

def criar_novo_jogo(linha,coluna):

    msg = {
        "acao": "criar_jogo",
        "linha": linha,
        "coluna":coluna
    }

    text = str(msg)
    text = enviar_servidor(text)
    rsp = literal_eval(text)

    if rsp["resposta"] != "sucesso":
        pass

def jogada(linha,coluna):
    pass