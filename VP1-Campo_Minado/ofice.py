
import sys, os
import random
from ast import literal_eval


menu_actions = {}

def iniciarMatriz(row,col):
    matriz = [["*" for x in range(row)] for y in range(col)] # l -> linhas ; c -> colunas
    return matriz

def exibirMatriz (matriz,row):
    print("")
    for i in range(row):
        print(matriz[i])

def espalharBombas(numero,row,col):
    vetor = []
    for i in range(numero): 
        i = random.randint(0,row-1) 
        numero = random.randint(0,col-1) 
        while ([i,numero] in vetor):
            i = random.randint(0,row-1) 
            numero = random.randint(0,col-1) 
        vetor.append([i,numero])
        
    return vetor

def bombasAoRedor(row,col,posBombas):
    cont = 0
    if ([row+1,col] in posBombas):
        cont += 1
    if ([row-1,col] in posBombas):
        cont += 1
    if ([row,col-1] in posBombas):
        cont += 1
    if ([row-1,col-1] in posBombas):
        cont += 1
    if ([row+1,col-1] in posBombas):
        cont += 1
    if ([row-1,col+1] in posBombas):
        cont += 1
    if ([row+1,col+1] in posBombas):
        cont += 1
    if ([row,col+1] in posBombas):
        cont += 1
    return cont;

def saveDados(historico):
    hist = open('log_game.txt', 'w')
    hist.write(str(historico))
    hist.close()

def verAquivo():
    arquivo = open('log_game.txt', 'r', encoding='UTF-8')
    dados = literal_eval(arquivo.read())
    arquivo.close()
    return dados

def painel(): 
    print("==================================================")
    print("                   CAMPO MINADO")
    print("==================================================\n")
    print("1. Para inciar um novo jogo")
    print("0. Sair")

def fimdeJogo():
    print("\n\n====@================================@===========")
    
    print("============@ BOUUUHHH! Você perdeu @============")
    
    print("====@================================@===========\n\n")

def vitoria():
    print("\n\nPARABÉNS!!! Você ganhou o desafio.")
    

def restart():
    os.system("cls")
    print("====================================================")
    print("                   CAMPO MINADO")
    print("====================================================\n")
    print("\nVocê possui um jogo em andamento!!!Deseja continuar?\n1: Para Sim\n2: Para Não\n")


def main_menu():
    if os.path.exists("log_game.txt") == True:
        dict = verAquivo()
        if (dict.get('without') == "-1"):
            painel()
            choice = input(" >> ")
            exec_menu(choice)
            return
        else:
            restartGame()
    else:
        painel()
        choice = input(" >> ")
        exec_menu(choice)
        return

def exec_menu(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Seleção inválida, por favor tentar novamente. \n")
            os.system("pause")
            menu_actions['main_menu']()
    return

def jogar():
    os.system("cls")
    print("==================================================")
    print("                   CAMPO MINADO")
    print("==================================================\n")
    estado = False
    jogadas = 0
    rowsMatriz = int(input("Digite quantas linhas deseja >> "))
    colsMatriz = int(input("Digite quantas colunas deseja >> "))
    quantidadeBombas = int(input("Digite a quantidade de bombas >> "))
    matriz = iniciarMatriz(rowsMatriz, colsMatriz)
    exibirMatriz (matriz, rowsMatriz)
    posBombas = espalharBombas(quantidadeBombas, rowsMatriz, colsMatriz)
    qtdJogadas = ((rowsMatriz * colsMatriz) - len(posBombas))
    while (estado == False):
        print("\nJogadas: %d | Jogadas restantes: %d" % (jogadas, qtdJogadas))
        linha = int(input("\nDigite a linha >> ")) - 1
        coluna = int(input("Digite a coluna >> ")) - 1
        os.system("cls")
        if ([linha, coluna] in posBombas):
            fimdeJogo()
            historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                         "colunasMatriz": 0, "without": "-1"}
            os.system("pause")
            menu_actions['main_menu']()
        else:
            matriz[linha][coluna] = str(bombasAoRedor(linha, coluna, posBombas))
            exibirMatriz(matriz, rowsMatriz)
            jogadas += 1
            qtdJogadas -= 1
            historico = {"matriz": matriz, "posBombas": posBombas, "jogadas": jogadas, "qtdJogadas": qtdJogadas,
                         "linhasMatriz": rowsMatriz, "colunasMatriz": colsMatriz, "without": 0}
            if (((rowsMatriz * colsMatriz) - jogadas) == len(posBombas)):
                vitoria()
                historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                             "colunasMatriz": 0, "without": "-1"}
                saveDados(historico)
                os.system("pause")
                menu_actions['main_menu']()
            saveDados(historico)
    return

def restartGame():
    restart()
    choice = int(input(" >> "))
    if (choice == 2):
        os.system("cls")
        historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                     "colunasMatriz": 0, "without": "-1"}
        saveDados(historico)
        jogar()
    else:
        
            return


def back():
    menu_actions['main_menu']()


def exit():
    print("\nFalou! ")
    os.system("pause")
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': jogar,
    '9': back,
    '0': exit,
}


if __name__ == "__main__":
    # Launch main menu
    main_menu()