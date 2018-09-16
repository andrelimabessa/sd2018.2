from campominado import CampoMinado
from os.path import isfile
from os import remove
import json
import sys

tabuleiro = CampoMinado(4,4)

def menu():
    print("1 - INICIAR JOGO                         ")
    print("2 - RESTAURAR                            ")
    print("3 - SAIR                                 ")
    opcao = int(input("Digite uma Opção :"))
    if opcao == 1:
        start()
    elif opcao == 2:
        partida()
    else:
        pass

def start ():
    if tabuleiro.proximaJogada():
        tabuleiro.imprimirTabuleiro()
        linha = int(input("Digite a posição da linha :"))
        coluna = int(input("Digite a posição da coluna :"))
        tabuleiro.jogada(linha,coluna)
        start()
    else:
        print("this is THE END")


def partida():
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        tabuleiro.restaurar(game)
        arquivo.close()
        start()
    else:
        print("Não existe Jogo salvo!\n")

menu()