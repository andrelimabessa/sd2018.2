from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json
import sys
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS



INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"



def menu_inicial():
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")


""" FIM MENU"""

def start ():
    if objeto.proxima_jogada():
        objeto.imprimir_tabuleiro()
        linha = int(input("Posição da linha :"))
        coluna = int(input("Posição da coluna :"))
        objeto.jogada(linha,coluna)
        start()
    else:
        print("Fim")


def partida():
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        objeto.restaurar(game)
        arquivo.close()
        start()
    else:
        print("Não há jogo salvo !\n")




def iniciar_novo_jogo(contexto):

    contexto[QUANTIDADE_LINHAS] = input("Informe a quantidade de linhas: ")
    contexto[QUANTIDADE_COLUNAS] = input("Informe a quantidade de colunas: ")

    return str(contexto)

def continuar_jogo(contexto):
    pass

def efetuar_nova_jogada(contexto):
    pass

def sair(contexto):
    sys.exit(0)


