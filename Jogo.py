import random
import re
import time
from string import ascii_lowercase
from CampoMinado import CampoMinado

def mostrarMina(mina):
    tamanho = len(mina)

    topo = '     '
    for idx, i in enumerate(mina):
        topo = topo + str(idx) + '    '
    print(topo + '\n')

    for idx, i in enumerate(mina):
        row = str(idx) + ' ||'
        for j in i:
            row = str(row) + ' ' + str(j) + ' ||'

        print(row + '\n')
    print('')

def selecionarCampo(mina, coluna, linha):
    return mina.clicarNaMina(coluna, linha)

def salvarMina(mina):
    arquivo = open("minaSalva.txt", "w")
    
    for item in mina:
        arquivo.write("%s\n" % item)
    arquivo.close()

def obterMinaSalva(tamanho):
    mina = [[' ' for i in range(tamanho)] for i in range(tamanho)]
    minaJogavel = [[' ' for i in range(tamanho)] for i in range(tamanho)]
    try:
        arquivo = open("minaSalva.txt", "r")
        idx=0
        for linha in arquivo:
            string = linha.replace("[", "")
            string = string.replace("]", "")
            string = string.replace("'", "")
            string = string.replace("\n", "")
            array = string.split(",")
            
            for i in range(tamanho):

                jogada = array[i].replace(" ", "")
                if(jogada != 'X'):
                    minaJogavel[idx][i] = jogada
                mina[idx][i] = jogada

            idx = idx + 1
        arquivo.close()
        return (mina, minaJogavel)
    except:
        return None

def jogar():
    tamanho = 10
    numeroMinas = 5

    mina = CampoMinado(tamanho, numeroMinas)
    gameOver = False

    minaJogavel = [[' ' for i in range(tamanho)] for i in range(tamanho)]

    while True: 
        mostrarMina(minaJogavel)
        
        print("MENU")
        print("0 - Carregar Mina Salva ")
        print("1 - Escolher um campo ")
        print("2 - Salvar e sair ")
        print("3 - Ver resposta ")

        escolha = input("ENTRE COM SUA ESCOLHA \n")

        if(escolha == 0):
            minaSalva, minaJogavelSalva = obterMinaSalva(tamanho)
            if(minaSalva != None):
                mina.carregarMina(minaSalva)
                minaJogavel = minaJogavelSalva
                print('MINA CARREGADA....')
            else:
                print('ERRO AO CARREGAR MINA, TEM CERTEZA QUE SALVOU UM JOGO?')
        elif(escolha == 1):
            coluna = input("SELECIONE A COLUNA \n")
            linha = input("SELECIONE A LINHA \n")
            resultado = selecionarCampo(mina, coluna, linha)
            if(resultado == "X"):
                gameOver = True
                break
            else:
                minaJogavel[linha][coluna] = resultado
        elif(escolha == 2):
            salvarMina(mina.obterMina())
            break
        elif(escolha == 3):
            mostrarMina(mina.obterMina())
        else:
            print('ESCOLHA INVALIDA \n')

    if(gameOver == True):
        print('Voce estorou uma bomba. Fim de Jogo')
    else:
        print('Voce saiu do jogo.')

jogar()


        
