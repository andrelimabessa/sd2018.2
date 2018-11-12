"""A command line version of minasweeper"""
import random
import re
import time
from string import ascii_lowercase


def montarCampo(tamanho, start, numeroDeMinas):
    campoVazio = [['0' for i in range(tamanho)] for i in range(tamanho)]

    Minas = getMinas(campoVazio, start, numeroDeMinas)

    for i, j in Minas:
        campoVazio[i][j] = 'X'

    campo = getNumeros(campoVazio)

    return (campo, Minas)


def mostrarCampo(campo):
    tamanhoDoCampo = len(campo)

    horizontal = '   ' + (4 * tamanhoDoCampo * '-') + '-'
    linhaSuperior = '     '
    
    for i in ascii_lowercase[:tamanhoDoCampo]:
        linhaSuperior = linhaSuperior + i + '   '

    print(linhaSuperior + '\n' + horizontal)

    for x, i in enumerate(campo):
        linha = '{0:2} |'.format(x + 1)

        for j in i:
            linha = linha + ' ' + j + ' |'

        print(linha + '\n' + horizontal)

    print('')


def getRadomValor(campo):
    tamanhoDoCampo = len(campo)

    a = random.randint(0, tamanhoDoCampo - 1)
    b = random.randint(0, tamanhoDoCampo - 1)

    return (a, b)


def getVizinhos(campo, linhaEscolhida, colunaEscolhida):
    tamanhoDoCampo = len(campo)
    vizinhos = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (linhaEscolhida + i) < tamanhoDoCampo and -1 < (colunaEscolhida + j) < tamanhoDoCampo:
                vizinhos.append((linhaEscolhida + i, colunaEscolhida + j))

    return vizinhos


def getMinas(campo, start, numeroDeMinas):
    minas = []
    vizinhos = getVizinhos(campo, *start)

    for i in range(numeroDeMinas):
        valor = getRadomValor(campo)
        while valor == start or valor in minas or valor in vizinhos:
            valor = getRadomValor(campo)
        minas.append(valor)

    return minas


def getNumeros(campo):
    for linhaEscolhida, row in enumerate(campo):
        for colunaEscolhida, valor in enumerate(row):
            if valor != 'X':
                values = [campo[r][c] for r, c in getVizinhos(campo,
                                                              linhaEscolhida, colunaEscolhida)]

                campo[linhaEscolhida][colunaEscolhida] = str(values.count('X'))

    return campo


def showValores(campo, campoAtual, linhaEscolhida, colunaEscolhida):
    if campoAtual[linhaEscolhida][colunaEscolhida] != ' ':
        return
    campoAtual[linhaEscolhida][colunaEscolhida] = campo[linhaEscolhida][colunaEscolhida]
    
    if campo[linhaEscolhida][colunaEscolhida] == '0':
        for r, c in getVizinhos(campo, linhaEscolhida, colunaEscolhida):
            if campoAtual[r][c] != 'F':
                showValores(campo, campoAtual, r, c)


def jogarDeNovo():
    escolha = input('Jogar de novo? (s/n): ')

    return escolha.lower() == 's'


def enviarResposta(resposta, tamanho, mensagemDeAjuda):
    cell = ()
    flag = False
    message = "Escolha invalida. " + mensagemDeAjuda

    pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[tamanho - 1])
    escolhaValida = re.match(pattern, resposta)

    if resposta == 'ajuda':
        message = mensagemDeAjuda

    elif escolhaValida:
        linhaEscolhida = int(escolhaValida.group(2)) - 1
        colunaEscolhida = ascii_lowercase.index(escolhaValida.group(1))
        flag = bool(escolhaValida.group(3))

        if -1 < linhaEscolhida < tamanho:
            cell = (linhaEscolhida, colunaEscolhida)
            message = ''

    return {'cell': cell, 'flag': flag, 'message': message}


def jogar():
    tamanho = 20
    numeroDeMinas = 10

    campoAtual = [[' ' for i in range(tamanho)] for i in range(tamanho)]

    campo = []
    flags = []
    starttime = 0

    mensagemDeAjuda = ("Digite a coluna seguida da linha. ex: a1 \n"
                   "Para adicionar uma flag coloque um f no final. ex: aif \n")

    mostrarCampo(campoAtual)
    print(mensagemDeAjuda + "Digite 'ajuda' para exibir essa mensagem novamente.\n")

    while True:
        minasRestantes = numeroDeMinas - len(flags)
        resposta = input('Selecione sua escolha ({} minas restantes): '.format(minasRestantes))
        result = enviarResposta(resposta, tamanho, mensagemDeAjuda + '\n')

        message = result['message']
        cell = result['cell']

        if cell:
            print('\n\n')
            linhaEscolhida, colunaEscolhida = cell
            escolhaAtual = campoAtual[linhaEscolhida][colunaEscolhida]
            flag = result['flag']

            if not campo:
                campo, minas = montarCampo(tamanho, cell, numeroDeMinas)
            if not starttime:
                starttime = time.time()

            if flag:
                if escolhaAtual == ' ':
                    campoAtual[linhaEscolhida][colunaEscolhida] = 'F'
                    flags.append(cell)
                elif escolhaAtual == 'F':
                    campoAtual[linhaEscolhida][colunaEscolhida] = ' '
                    flags.remove(cell)
                else:
                    message = 'Não pode colocar uma flag aqui'

            elif cell in flags:
                message = 'Tem uma flag ali'

            elif campo[linhaEscolhida][colunaEscolhida] == 'X':
                print('Game Over\n')
                mostrarCampo(campo)
                if jogarDeNovo():
                    jogar()
                return

            elif escolhaAtual == ' ':
                showValores(campo, campoAtual, linhaEscolhida, colunaEscolhida)

            else:
                message = "Essa escolha já está sendo exibida"

            if set(flags) == set(minas):
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print(
                    'Você venceu. '
                    'Você levou {} minutos e {} segundos.\n'.format(minutes,
                                                                      seconds))
                mostrarCampo(campo)
                if jogarDeNovo():
                    jogar()
                return

        mostrarCampo(campoAtual)
        print(message)

jogar()