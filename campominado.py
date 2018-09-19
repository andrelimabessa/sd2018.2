import random
import re
import time
from string import ascii_lowercase


def configurarCampo(tamanhoDoCampo, start, numeroDeBombas):
    gradeVazia = [['0' for i in range(tamanhoDoCampo)] for i in range(tamanhoDoCampo)]

    minas = gerarMinas(gradeVazia, start, numeroDeBombas)

    for i, j in minas:
        gradeVazia[i][j] = 'X'

    grade = gerarNumeros(gradeVazia)

    return (grade, minas)


def gerarCampo(grade):
    tamanhoDoCampo = len(grade)

    horizontal = '   ' + (4 * tamanhoDoCampo * '') + ''
    coluna = '     '
    
    for i in ascii_lowercase[:tamanhoDoCampo]:
        coluna = coluna + i + '   '

    print(coluna + '\n' + horizontal)

    for x, i in enumerate(grade):
        linha = '{0:2} '.format(x + 1)

        for j in i:
            linha = linha + ' ' + j + ' |'

        print(linha + '\n' + horizontal)

    print('')


def pegarPosicaoAleatoria(grade):
    tamanhoDoCampo = len(grade)

    a = random.randint(0, tamanhoDoCampo - 1)
    b = random.randint(0, tamanhoDoCampo - 1)

    return (a, b)


def getVizinhos(grade, linha, coluna):
    tamanhoDoCampo = len(grade)
    vizinhos = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (linha + i) < tamanhoDoCampo and -1 < (coluna + j) < tamanhoDoCampo:
                vizinhos.append((linha + i, coluna + j))

    return vizinhos


def gerarMinas(grade, start, numeroDeBombas):
    minas = []
    vizinhos = getVizinhos(grade, *start)

    for i in range(numeroDeBombas):
        celula = pegarPosicaoAleatoria(grade)
        while celula == start or celula in minas or celula in vizinhos:
            celula = pegarPosicaoAleatoria(grade)
        minas.append(celula)

    return minas


def gerarNumeros(grade):
    for linha, row in enumerate(grade):
        for coluna, celula in enumerate(row):
            if celula != 'X':
                values = [grade[r][c] for r, c in getVizinhos(grade,
                                                              linha, coluna)]

                grade[linha][coluna] = str(values.count('X'))

    return grade


def mostrarCampos(grade, tabuleiroAtual, linha, coluna):
    if tabuleiroAtual[linha][coluna] != ' ':
        return
    tabuleiroAtual[linha][coluna] = grade[linha][coluna]
    
    if grade[linha][coluna] == '0':
        for r, c in getVizinhos(grade, linha, coluna):
            if tabuleiroAtual[r][c] != 'F':
                mostrarCampos(grade, tabuleiroAtual, r, c)


def _jogarDeNovo():
    escolha = input('Jogar novamente? (s/n): ')

    return escolha.lower() == 's'


def enviarResposta(resposta, tamanhoDoCampo, mensagemDeAjuda):
    celula = ()
    message = "Escolha invalida. " + mensagemDeAjuda

    pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[tamanhoDoCampo - 1])
    escolhaValida = re.match(pattern, resposta)

    if resposta == 'ajuda':
        message = mensagemDeAjuda

    elif escolhaValida:
        linha = int(escolhaValida.group(2)) - 1
        coluna = ascii_lowercase.index(escolhaValida.group(1))
        
        if -1 < linha < tamanhoDoCampo:
            celula = (linha, coluna)
            message = ''

    return {'celula': celula, 'message': message}


def jogar():
    tamanhoDoCampo = 5
    numeroDeBombas = 7

    tabuleiroAtual = [[' ' for i in range(tamanhoDoCampo)] for i in range(tamanhoDoCampo)]

    grade = []
    tempoInicial = 0

    mensagemDeAjuda = ("Digite a coluna e a linha. \n")

    gerarCampo(tabuleiroAtual)

    while True:
        minasRestantes = numeroDeBombas
        resposta = input('Selecione sua escolha ({} minas restantes): '.format(minasRestantes))
        result = enviarResposta(resposta, tamanhoDoCampo, mensagemDeAjuda + '\n')

        message = result['message']
        celula = result['celula']

        if celula:
            print('\n\n')
            linha, coluna = celula
            escolhaAtual = tabuleiroAtual[linha][coluna]
 
            if not grade:
                grade, minas = configurarCampo(tamanhoDoCampo, celula, numeroDeBombas)
            if not tempoInicial:
                tempoInicial = time.time()

            elif grade[linha][coluna] == 'X':
                print('Você Perdeu\n')
                gerarCampo(grade)
                if _jogarDeNovo():
                    jogar()
                return

            elif escolhaAtual == ' ':
                mostrarCampos(grade, tabuleiroAtual, linha, coluna)

            else:
                message = "Essa escolha já está sendo exibida"

            if set(minas) == 0:
                minutos, segundos = divmod(int(time.time() - tempoInicial), 60)
                print(
                    'Você venceu! '
                    'Você levou {} minutos e {} segundos.\n'.format(minutos,
                                                                      segundos))
                gerarCampo(grade)
                if _jogarDeNovo():
                    jogar()
                return

        gerarCampo(tabuleiroAtual)
        print(message)

jogar()