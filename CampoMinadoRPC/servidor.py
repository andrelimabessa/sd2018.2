import socket
from datetime import datetime
from ast import literal_eval
from os.path import isfile
from os import remove
import json
from campo_minado_negocio import CampoMinado
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_FALHA, RESPOSTA_SUCESSO ,JOGADA_COLUNA, JOGADA_LINHA , CODIGO_COMANDO, COMANDO_EFETUAR_JOGADA, COMANDO_SHOW, IMPRIMIR, QTD

def servidor():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_novo_jogo)
    serverRPC.register_function(tabuleiro_show)
    print("Starting server")
    serverRPC.serve_forever()


def tabuleiro_show(jogo,contexto):
    tabuleiro = jogo.tabuleiro_show()
    return str(tabuleiro)

def quatidade(jogo,contexto):
    jogadas = jogo.qtd_jogadas()
    return str(jogadas)


def jogada(jogo,contexto):
    #print("JOGADA() CONTEXTO  ", contexto)
    linha = int(contexto.get(JOGADA_LINHA))
    coluna = int(contexto.get(JOGADA_COLUNA))
    #print("LINHA ",linha," COLUNA ",coluna)
    jogo.jogada(linha,coluna)
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

def restaurar_jogo(jogo,contexto):
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        jogo.restaurar(game)
        arquivo.close()

def criar_novo_jogo(serverRPC,contexto):

    linha = int(contexto.get(QUANTIDADE_LINHAS))
    coluna = int(contexto.get(QUANTIDADE_COLUNAS))

    #print(linha,coluna)
    jogo.criar_novo_jogo(linha,coluna)
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

if __name__ == "__main__":
    servidor()
