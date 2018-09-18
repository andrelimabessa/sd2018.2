# CampoMinado (Nota complementar Sistemas Distribuídos)
# Aluno: Edelucio Antônio Alves Luciano
import sys
import os
import random
from ast import literal_eval

menu_actions = {}

# Gerar Matriz
def gerarMatriz(l, c):
    matriz = [["*" for x in range(l)] for y in range(c)]
    return matriz

# Mostrar Matriz
def mostrarMatriz(matriz, l):
    print("")
    for i in range(l):
        print(matriz[i])

# Sortear Bombas
def sortearBombas(n, l, c):
    vetor = []
    for i in range(n):
        i = random.randint(0, l - 1)  # y -1
        n = random.randint(0, c - 1)  # x -1
        while ([i, n] in vetor):
            i = random.randint(0, l - 1)  # y -1
            n = random.randint(0, c - 1)  # x -1
        vetor.append([i, n])
        # print(vetor)
    return vetor

# Bombas ao Redor
def bombasAoRedor(l, c, posBombas):
    count = 0
    if ([l + 1, c] in posBombas):
        count += 1
    if ([l - 1, c] in posBombas):
        count += 1
    if ([l, c - 1] in posBombas):
        count += 1
    if ([l - 1, c - 1] in posBombas):
        count += 1
    if ([l + 1, c - 1] in posBombas):
        count += 1
    if ([l - 1, c + 1] in posBombas):
        count += 1
    if ([l + 1, c + 1] in posBombas):
        count += 1
    if ([l, c + 1] in posBombas):
        count += 1
    return count

# Salvando hitórico do jogo
def save(historico):
    hist = open('log_game.txt', 'w')
    hist.write(str(historico))
    hist.close()

# Abrindo e lendo o histórico do jogo
def verifyFile():
    arquivo = open('log_game.txt', 'r', encoding='UTF-8')
    dados = literal_eval(arquivo.read())
    arquivo.close()
    return dados

# Menu
def layout():
    print("\n*** CAMPO MINADO ***\n")
    print("Escolha um opção: 1 ou 0\n")
    print("1. Jogar")
    print("0. Sair")

# Final do jogo
def gameOver():
    print("\n   VOCÊ PERDEU!!!   \n")

# Ganhou o jogo
def win():
    print("\n   VOCÊ GANHOU!!!   \n")

# Reinicia um jogo em andamento
def restart():
    os.system("cls")
    print("\n*** CAMPO MINADO ***\n")
    print("\nVocê possui um jogo em andamento. Deseja continuar?\n1: Para Sim\n2: Para Não\n")

# Main menu
def main_menu():
    if os.path.exists("log_game.txt") == True:
        dict = verifyFile()
        if (dict.get('without') == "-1"):
            layout()
            choice = input(" >> ")
            exec_menu(choice)
            return
        else:
            restartGame()
    else:
        layout()
        choice = input(" >> ")
        exec_menu(choice)
        return

# Seleção inválida
def exec_menu(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("\nSeleção inválida! Favor tentar novamente!\n")
            os.system("pause")
            menu_actions['main_menu']()
    return

# Novo jogo
def newGame():
    os.system("cls")
    print("\n*** CAMPO MINADO ***\n")
    perdeu = False
    jogadas = 0
    linhasMatriz = int(input("Digite quantidade de linhas: "))
    colunasMatriz = int(input("Digite quantidade de colunas: "))
    quantidadeBombas = int(input("Digite quantidade de bombas: "))
    matriz = gerarMatriz(linhasMatriz, colunasMatriz)
    mostrarMatriz(matriz, linhasMatriz)
    posBombas = sortearBombas(quantidadeBombas, linhasMatriz, colunasMatriz)
    qtdJogadas = ((linhasMatriz * colunasMatriz) - len(posBombas))
    while (perdeu == False):
        print("\nJogadas: %d | Jogadas restantes: %d" % (jogadas, qtdJogadas))
        linha = int(input("\nDigite a linha >> ")) - 1
        coluna = int(input("Digite a coluna >> ")) - 1
        os.system("cls")
        if ([linha, coluna] in posBombas):
            gameOver()
            historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                         "colunasMatriz": 0, "without": "-1"}
            os.system("pause")
            menu_actions['main_menu']()
        else:
            matriz[linha][coluna] = str(
                bombasAoRedor(linha, coluna, posBombas))
            mostrarMatriz(matriz, linhasMatriz)
            jogadas += 1
            qtdJogadas -= 1
            historico = {"matriz": matriz, "posBombas": posBombas, "jogadas": jogadas, "qtdJogadas": qtdJogadas,
                         "linhasMatriz": linhasMatriz, "colunasMatriz": colunasMatriz, "without": 0}
            if (((linhasMatriz * colunasMatriz) - jogadas) == len(posBombas)):
                win()
                historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                             "colunasMatriz": 0, "without": "-1"}
                save(historico)
                os.system("pause")
                menu_actions['main_menu']()
            save(historico)
    return

# Reiniciar jogo
def restartGame():
    restart()
    choice = int(input(" >> "))
    if (choice == 2):
        os.system("cls")
        historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                     "colunasMatriz": 0, "without": "-1"}
        save(historico)
        newGame()
    else:
        dict = verifyFile()
        if (dict.get('without') == "-1"):
            print("\nNão existe nenhum jogo salvo!\n")
            print("\nVocê deseja iniciar um novo jogo?\n1: para Sim \n2: para não")
            answer = int(input("\n S ou N:"))
            if (answer == 1):
                os.system("cls")
                newGame()
            else:
                print("\nMUITO BOM JOGAR COM VOCÊ!\n")
                os.system("pause")
                menu_actions['main_menu']()
        else:
            matriz = dict.get('matriz')
            posBombas = dict.get('posBombas')
            jogadas = dict.get('jogadas')
            linhasMatriz = dict.get('linhasMatriz')
            colunasMatriz = dict.get('colunasMatriz')
            qtdJogadas = dict.get('qtdJogadas')
            perdeu = False
            mostrarMatriz(matriz, linhasMatriz)
            while (perdeu == False):
                print("\nJogadas: %d | Jogadas restantes: %d" %
                      (jogadas, qtdJogadas))
                linha = int(input("\nDigite a linha >> ")) - 1
                coluna = int(input("Digite a coluna >> ")) - 1
                os.system("cls")
                if ([linha, coluna] in posBombas):
                    gameOver()
                    historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                                 "colunasMatriz": 0, "without": "-1"}
                    save(historico)
                    os.system("pause")
                    os.system("cls")
                    menu_actions['main_menu']()
                else:
                    matriz[linha][coluna] = str(
                        bombasAoRedor(linha, coluna, posBombas))
                    mostrarMatriz(matriz, linhasMatriz)
                    jogadas += 1
                    qtdJogadas -= 1
                    historico = {"matriz": matriz, "posBombas": posBombas, "jogadas": jogadas, "qtdJogadas": qtdJogadas,
                                 "linhasMatriz": linhasMatriz, "colunasMatriz": colunasMatriz, "without": 0}
                    if (((linhasMatriz * colunasMatriz) - jogadas) == len(posBombas)):
                        print("\n\nVOCÊ GANHOU!")
                        historico = {"matriz": 0, "posBombas": 0, "jogadas": 0, "qtdJogadas": 0, "linhasMatriz": 0,
                                     "colunasMatriz": 0, "without": "-1"}
                        save(historico)
                        os.system("cls")
                        os.system("pause")
                        menu_actions['main_menu']()
                    save(historico)
            return

# Retorna ao main menu
def back():
    menu_actions['main_menu']()

# Sair do jogo
def exit():
    print("\nMUITO BOM JOGAR COM VOCÊ!\n")
    os.system("pause")
    sys.exit()

# Menu
menu_actions = {
    'main_menu': main_menu,
    '1': newGame,
    '2': restartGame,
    '9': back,
    '0': exit,
}

# Programa main
if __name__ == "__main__":
    # Main menu
    main_menu()
