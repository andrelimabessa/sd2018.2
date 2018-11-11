#import socket
import zmq
import time
import sys
import random
from ast import literal_eval
import threading
from datetime import datetime
from campo_minado_negocio import CampoMinado
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_FALHA, RESPOSTA_SUCESSO ,JOGADA_LINHA , CODIGO_COMANDO, COMANDO_EFETUAR_JOGADA, COMANDO_SHOW, IMPRIMIR, QTD


try:
    port = "5560"
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % port)
    server_id = random.randrange(1,10005)
    ENCODE = "UTF-8"

    jogo = CampoMinado()

    while True:
        #  Espera pela próxima requisição do cliente
        data = socket.recv()
        mensagem = data.decode(ENCODE)           # Convertendo dados de BASE64 para UTF-8
        contexto = literal_eval(mensagem)
        #Trata comando recebido por algum cliente
        resposta = tratar_mensagem(jogo, contexto)
        time.sleep (1)
        data = resposta.encode(ENCODE) # Codifica para BASE64 os dados
        socket.send(data)

    def tratar_mensagem(jogo, contexto):

        codigo = contexto["codigo_comando"]
        #print("CODIGO =  ",codigo)
        switch = {
        "1": criar_novo_jogo,
        "efetuar_jogada":jogada,
        "jogadas":quatidade,
        "tabuleiro":tabuleiro_show
        }
        func = switch.get(str(codigo))
        print("IMPRIMIR CONTEXTO ",contexto)
        #Todas as funções devem receber
        return func(jogo, contexto)


    def tabuleiro_show(jogo,contexto):
        tabuleiro = jogo.tabuleiro_show()
        return str(tabuleiro)

    def quatidade(jogo,contexto):
        jogadas = jogo.qtd_jogadas()
        return str(jogadas)


    def jogada(jogo,contexto):
 
        linha = int(contexto.get(JOGADA_LINHA))
        coluna = int(contexto.get(JOGADA_LINHA))
        jogo.jogada(linha,coluna)
        return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})


    def criar_novo_jogo(jogo,contexto):

        linha = int(contexto.get(QUANTIDADE_LINHAS))
        coluna = int(contexto.get(QUANTIDADE_COLUNAS))

        #print(linha,coluna)
        jogo.criar_novo_jogo(linha,coluna)
        jogo.tabuleiro_show()
        tabu = jogo.tabuleiro_show()

        return str(tabu)


except:
    for val in sys.exc_info():
        print(val)

input("Saida Enter")