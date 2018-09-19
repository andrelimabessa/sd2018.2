from random import randint
import re
from string import ascii_lowercase

def configTabuleiro(QuantidadeCelulas, celula, QuantidadeMinas):
    tabuleiroVazio = [['0' for i in range(QuantidadeCelulas)] for i in range(QuantidadeCelulas)]

    minas = pegarMinas(tabuleiroVazio, celula, QuantidadeMinas)

    for i, j in minas:
        tabuleiroVazio[i][j] = 'X'

    grid = pegarPontos(tabuleiroVazio)

    return (grid, minas)

def montarTabuleiro(tabuleiro):
    tamanhoTabuleiro = len(tabuleiro)

    # separamento de células
    horizontal = '   ' + (4 * tamanhoTabuleiro * '-') + '-'

    toplabel = '     '

    arquivo = open('text.txt', 'w')
    # Identificar colunas
    for i in ascii_lowercase[:tamanhoTabuleiro]:
        toplabel = toplabel + i + '   '
        test = toplabel + '\n'
    arquivo.writelines(test)
    print(toplabel + '\n' + horizontal)

    # Identificar linhas
    for idx, i in enumerate(tabuleiro):
        row = '{0:2} |'.format(idx + 1)
        # barras separamento
        for j in i:
            row = row + ' ' + j + ' |'
            test = row + '\n'
            test2 = horizontal +'\n'
        arquivo.writelines(test) 
        arquivo.writelines(test2)
        print(row + '\n' + horizontal)
    arquivo.close()
    print('')

def escolhaCelulaRandom(tabuleiroVazio):
    tamanhoTabuleiro = len(tabuleiroVazio)

    x = randint(0, tamanhoTabuleiro - 1)
    y = randint(0, tamanhoTabuleiro - 1)

    return (x,y)

def pegarVizinhos(tabuleiroVazio, numero_linha, numero_coluna):
    tamanhoTabuleiro = len(tabuleiroVazio)
    vizinhos = []
    
    for x in range(-1,2):
        for y in range(-1,2):
            if x == 0 and y == 0:
                continue
            elif -1 < (numero_linha + x) < tamanhoTabuleiro and -1 < (numero_coluna + y) < tamanhoTabuleiro:
                vizinhos.append((numero_linha + x, numero_coluna+ y))
    return vizinhos

def pegarMinas(tabuleiroVazio, inicio, QuantidadeMinas):
    minas = []
    vizinhos = pegarVizinhos(tabuleiroVazio, *inicio)

    for i in range(QuantidadeMinas):
        celula = escolhaCelulaRandom(tabuleiroVazio)
        while celula == inicio or celula in minas or celula in vizinhos:
            celula = escolhaCelulaRandom(tabuleiroVazio)
        minas.append(celula)
    return minas

def pegarPontos(tabuleiroVazio):
    for numero_linha, linha in enumerate(tabuleiroVazio):
        for numero_coluna, celula in enumerate(linha):
            if celula != 'X':
                # Gets the values of the neighbors
                valores = [tabuleiroVazio[r][c] for r, c in pegarVizinhos(tabuleiroVazio,numero_linha, numero_coluna)]

                # Counts how many are mines
                tabuleiroVazio[numero_linha][numero_coluna] = str(valores.count('X'))
    return tabuleiroVazio

def mostrarCelulas(tabuleiroVazio, tabuleiro, numero_linha, numero_coluna):
    if tabuleiro[numero_linha][numero_coluna] != ' ':
        return
    
    tabuleiro[numero_linha][numero_coluna] = tabuleiroVazio[numero_linha][numero_coluna]

    if tabuleiroVazio[numero_linha][numero_coluna] == '0':
        for numero_linha, numero_coluna in pegarVizinhos(tabuleiroVazio, numero_linha, numero_coluna):
            if tabuleiro[numero_linha][numero_coluna] != 'F':
                mostrarCelulas(tabuleiroVazio, tabuleiro, numero_linha, numero_coluna)

def jogarNovamente():
    escolha = input('Jogar Novemente? (s/n): ')

    return escolha.lower() == 's'

def jogadaValida(entradaDados, QuantidadeCelulas, helpmessage):
    celula = ()
    bandeira = False
    mensagem = "Campo inválido " + helpmessage

    padrao = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[QuantidadeCelulas - 1])
    validacao_input = re.match(padrao, entradaDados)

    if entradaDados == 'help':
        mensagem = helpmessage

    elif validacao_input:
        numero_linha = int(validacao_input.group(2))-1
        numero_coluna = ascii_lowercase.index(validacao_input.group(1))
        bandeira = bool(validacao_input.group(3))

        if -1 < numero_linha and -1 < QuantidadeCelulas:
            celula = (numero_linha,numero_coluna)
            mensagem = ''

    return {'celula':celula, 'bandeira': bandeira, 'mensagem': mensagem}

def play():
    QuantidadeCelulas = int(input("Digite a quantidade de linhas/colunas do campo minado:"))
    QuantidadeMinas = randint(QuantidadeCelulas,(QuantidadeCelulas*2))

    tabuleiro = [[' ' for i in range(QuantidadeCelulas) ] for i in range(QuantidadeCelulas)]

    tb = []
    bandeiras = []
    
    helpmessage = ("Digite a coluna em seguida da linha (por exemplo, a5).")

    montarTabuleiro(tabuleiro)

    while True:
        minasRestante = QuantidadeMinas - len(bandeiras)
        prompt = input('Escolha a celula ({} minas existentes): '.format(minasRestante))
        resultado = jogadaValida(prompt, QuantidadeCelulas, helpmessage)

        mensagem = resultado['mensagem']
        celula = resultado['celula']

        if celula:
            print('\n\n')
            numero_linha, numero_coluna = celula
            celula_atual = tabuleiro[numero_linha][numero_coluna]
            bandeira = resultado['bandeira']

            if not tb:
                tb, minas = configTabuleiro(QuantidadeCelulas, celula, QuantidadeMinas)

            if bandeira:
                # Adiciona bandeira a celula vazia
                if celula_atual == ' ':
                    tabuleiro[numero_linha][numero_coluna] = 'F'
                    bandeiras.append(celula)
                # Remove a bandeira
                elif celula_atual == 'F':
                    tabuleiro[numero_linha][numero_coluna] = ' '
                    bandeiras.remove(celula)
                else:
                    mensagem = 'Cannot put a flag there'

            # If there is a flag there, show a message
            elif celula in bandeiras:
                mensagem = 'There is a flag there'

            elif celula_atual == ' ':
                mostrarCelulas(tb, tabuleiro, numero_linha, numero_coluna)

            else:
                mensagem = "That cell is already shown"

            if tb[numero_linha][numero_coluna] == 'X':
                print('Game Over\n')
                montarTabuleiro(tb)
                if jogarNovamente():
                    play()
                return   
play()