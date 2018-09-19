import random
import re
import time
from string import ascii_lowercase
from MineField_Logic import MineField

def showMine(mine):
    size = getSize(mine)

    top = '     	'
    for idx, i in enumerate(mine):
        top = top + str(idx) + '    	'
    print(top + '\n')

    for idx, i in enumerate(mine):
        row = str(idx) + ' |||'
        for j in i:
            row = str(row) + ' ' + str(j) + ' |||'

        print(row + '\n')
    print('')

def selectCell(mine, column, row):
    return mine.getClick(column, row)

def saveMine(mine):
    archive = open("lastGame.txt", "w")
    
    for item in mine:
        archive.write("%s\n" % item)
    archive.close()

def recoverGame(size):
    mine = [[' ' for i in range(size)] for i in range(size)]
    printableMine = [[' ' for i in range(size)] for i in range(size)]
    try:
        archive = open("lastGame.txt", "r")
        idx=0
        for row in archive:
            string = row.replace("[", "")
            string = string.replace("]", "")
            string = string.replace("'", "")
            string = string.replace("\n", "")
            array = string.split(",")
            
            for i in range(size):

                jogada = array[i].replace(" ", "")
                if(jogada != '#'):
                    printableMine[idx][i] = jogada
                mine[idx][i] = jogada

            idx = idx + 1
        archive.close()
        return (mine, printableMine)
    except:
        return None

def jogar():
    size = 10
    numMines = 5

    mine = MineField(size, numMines)
    gameOver = False

    printableMine = [[' ' for i in range(size)] for i in range(size)]

    while True: 
        mostrarmine(printableMine)
        
        print("MENU")
        print("0 - Carregar jogo salvo ")
        print("1 - Escolher um campo ")
        print("2 - Salvar ")
        print("3 - Sair ")

        choice = input("ENTRE COM SUA ESCOLHA \n")

        if(choice == 0):
            mineSalva, printableMineSalva = obtermineSalva(size)
            if(mineSalva != None):
                mine.carregarmine(mineSalva)
                printableMine = printableMineSalva
                print('JOGO CARREGADO....')
            else:
                print('ERRO AO CARREGAR JOGO, TEM CERTEZA POSSUI UM JOGO SALVO?')
        elif(choice == 1):
            column = input("SELECIONE A COLUNA \n")
            row = input("SELECIONE A LINHA \n")
            resultado = selectCell(mine, column, row)
            if(resultado == "#"):
                gameOver = True
                break
            else:
                printableMine[row][column] = resultado
        elif(choice == 2):
            saveMine(mine.getMine())
            print('JOGO SALVO....')
        elif(choice == 3):
            break
        else:
            print('ESCOLHA INVALIDA \n')

    if(gameOver == True):
        print('Game Over!')
    else:
        print('Voce saiu do jogo.')

jogar()


        
