import random
import re
import time
from string import ascii_lowercase

import random
import re
import time
from string import ascii_lowercase

import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):

    def exposed_line_counter(self, fileobj, function):
        #exposed_expoe o metodo
        print('Cliente chamou line counter')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_print_name(self, nome, sobrenome):
        return nome + " " + sobrenome
    
    def exposed_teste(self, nome, sobrenome):
        return nome + " - " + sobrenome

    def exposed_montarCampo(self, tamanho, start, numeroDeMinas):
        campoVazio = [['0' for i in range(tamanho)] for i in range(tamanho)]

        Minas = self.exposed_getMinas(campoVazio, start, numeroDeMinas)

        for i, j in Minas:
            campoVazio[i][j] = 'X'

        campo = self.exposed_getNumeros(campoVazio)

        return (campo, Minas)    


    def exposed_mostrarCampo(self, campo):
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

    def exposed_getRadomValor(self, campo):
        tamanhoDoCampo = len(campo)

        a = random.randint(0, tamanhoDoCampo - 1)
        b = random.randint(0, tamanhoDoCampo - 1)

        return (a, b)


    def exposed_getVizinhos(self, campo, linhaEscolhida, colunaEscolhida):
        tamanhoDoCampo = len(campo)
        vizinhos = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif -1 < (linhaEscolhida + i) < tamanhoDoCampo and -1 < (colunaEscolhida + j) < tamanhoDoCampo:
                    vizinhos.append((linhaEscolhida + i, colunaEscolhida + j))

        return vizinhos
    



    def exposed_getMinas(self, campo, start, numeroDeMinas):
        minas = []
        vizinhos = self.exposed_getVizinhos(campo, *start)

        for i in range(numeroDeMinas):
            valor = self.exposed_getRadomValor(campo)
            while valor == start or valor in minas or valor in vizinhos:
                valor = self.exposed_getRadomValor(campo)
            minas.append(valor)

        return minas


    def exposed_getNumeros(self, campo):
        for linhaEscolhida, row in enumerate(campo):
            for colunaEscolhida, valor in enumerate(row):
                if valor != 'X':
                    values = [campo[r][c] for r, c in self.exposed_getVizinhos(campo,
                                                                  linhaEscolhida, colunaEscolhida)]

                    campo[linhaEscolhida][colunaEscolhida] = str(values.count('X'))

        return campo

        

    def exposed_showValores(self, campo, campoAtual, linhaEscolhida, colunaEscolhida):
        if campoAtual[linhaEscolhida][colunaEscolhida] != ' ':
            return
        campoAtual[linhaEscolhida][colunaEscolhida] = campo[linhaEscolhida][colunaEscolhida]
        
        if campo[linhaEscolhida][colunaEscolhida] == '0':
            for r, c in self.exposed_getVizinhos(campo, linhaEscolhida, colunaEscolhida):
                if campoAtual[r][c] != 'F':
                    self.exposed_showValores(campo, campoAtual, r, c)

    

    def exposed_jogarDeNovo(self):
        escolha = input('Jogar de novo? (s/n): ')

        return escolha.lower() == 's'



    def exposed_enviarResposta(self, resposta, tamanho, mensagemDeAjuda):
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



    def exposed_jogar(self):
        tamanho = 20
        numeroDeMinas = 10

        campoAtual = [[' ' for i in range(tamanho)] for i in range(tamanho)]

        campo = []
        flags = []
        starttime = 0

        mensagemDeAjuda = ("Digite a coluna seguida da linha. ex: a1 \n"
                       "Para adicionar uma flag coloque um f no final. ex: aif \n")

        self.exposed_mostrarCampo(campoAtual)
        print(mensagemDeAjuda + "Digite 'ajuda' para exibir essa mensagem novamente.\n")

        while True:
            minasRestantes = numeroDeMinas - len(flags)
            resposta = input('Selecione sua escolha ({} minas restantes): '.format(minasRestantes))
            result = self.exposed_enviarResposta(resposta, tamanho, mensagemDeAjuda + '\n')

            message = result['message']
            cell = result['cell']

            if cell:
                print('\n\n')
                linhaEscolhida, colunaEscolhida = cell
                escolhaAtual = campoAtual[linhaEscolhida][colunaEscolhida]
                flag = result['flag']

                if not campo:
                    campo, minas = self.exposed_montarCampo(tamanho, cell, numeroDeMinas)
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
                    self.exposed_mostrarCampo(campo)
                    if self.exposed_jogarDeNovo():
                        self.exposed_jogar()
                    return

                elif escolhaAtual == ' ':
                    self.exposed_showValores(campo, campoAtual, linhaEscolhida, colunaEscolhida)

                else:
                    message = "Essa escolha já está sendo exibida"

                if set(flags) == set(minas):
                    minutes, seconds = divmod(int(time.time() - starttime), 60)
                    print(
                        'Você venceu. '
                        'Você levou {} minutos e {} segundos.\n'.format(minutes,
                                                                          seconds))
                    self.exposed_mostrarCampo(campo)
                    if self.exposed_jogarDeNovo():
                        self.exposed_jogar()
                    return

            self.exposed_mostrarCampo(campoAtual)
            print(message)
    


def server():    
    t = ThreadedServer(MyService, port = 18861)
    t.start()
