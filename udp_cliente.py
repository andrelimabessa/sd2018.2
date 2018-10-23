
import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos


def client():
    
    tamCampo = int(input("Informe o tamanho do campo (ex.: 5): "))
    nBombas = int(input("Informe a quantidade de Bombas no campo (ex.: 10): "))

    cm = inicio(tamCampo, tamCampo, nBombas)
    dados = {1: 1, 2: 2,3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    percorrerCampo(cm, dados)
    
'''
    data = [tamCampo, nBombas, start]
    data = str(data)
    data = data.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    #Enviando de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
    dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
    sock.sendto(data, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor

    print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
    text = data.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
    print(address, text)                        # Imprime texto e endereços

    #Fechando Socket
    sock.close()
'''
    
def inicio(nColuna, nLinha, nBombas):
    campoLimpo = [[0 for i in range(nColuna)] for i in range(nLinha)]
    mostrarCampo(campoLimpo)

    #print(campoLimpo)

    return campoLimpo


def mostrarCampo(campoAtual):
        print('\n')
        for linha in campoAtual:
            print(end=' | ')
            for coluna in linha:
                print(coluna, end=' | ')
                fim = '--' * len(linha) * 2
            print('\n', fim)
        print('\n')

def percorrerCampo(campoAtual, alteracoes):
    x = -1
    index = 1
    print(type(alteracoes))
    for l in campoAtual:
        print('vetor l', l)
        y = 0
        x = x + 1
        
        for c in l:
           
            #y < len(l)):
            print('numero:', c)
            print('len', len(l))
            valor = alteracoes[index]
            campoAtual[x][y] = valor

            index = index + 1               
            print('x:', x, '-', 'y:', y)
            y = y + 1 
            #else: 
                #y = 0   
                #print('valor de y no else', y)          
    
    
    print(campoAtual)
    mostrarCampo(campoAtual)



client()


    
        

