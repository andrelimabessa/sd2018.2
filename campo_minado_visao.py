from campo_minado_servico import CampoMinado
from os.path import isfile
from os import remove
import json
import sys






campo = CampoMinado(5, 5)




def menu():
    print("*****************************************")
    print("*              MINE FIELD               *")
    print("*****************************************")
    print("*1 - START                              *")
    print("*2 - RESTORE                            *")
    print("*3 - EXIT                               *")
    print("*****************************************\n")
    opcao = int(input("Inserir Opção :"))
    if opcao == 1:
        start()
    elif opcao == 2:
        partida()
    else:
        pass


def start ():
    if campo.proxima_jogada():
        campo.mostrar_tabuleiro()
        try:
            linha = int(input("Posição da linha :"))
        except ValueError:
            print("Digite apenas numeros!") 
            linha = int(input("Posição da linha :"))       
        try:
            coluna = int(input("Posição da coluna :"))
        except ValueError:
            print("Digite apenas numeros!")
            coluna = int(input("Posição da coluna :"))
        campo.jogada(linha,coluna)
        start()
    else:
        print("Saiu")


def partida():
    if isfile("jogo.json"):
        arquivo = open("jogo.json")
        jogo = json.loads(arquivo.read())
        campo.restaurar(jogo)
        arquivo.close()
        start()
    else:
        print("Você não tem jogo salvo!\n")



menu()
