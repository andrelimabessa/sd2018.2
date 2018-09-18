import persistencia
import random
from string import ascii_lowercase

class Campo:



    def __init__(self, nColuna, nLinha, nBombas):
        self.campoLimpo = [['-' for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = [[0 for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = self.gerarBombas(self.campoMinado, nBombas, nLinha, nColuna)
        self.nJogadas = nColuna * nLinha - nBombas
        #self.mostrarCampo(self.campoMinado)
        self.mostrarCampo(self.campoLimpo)
        
        self.jogada(self.campoLimpo, self.campoMinado, self.nJogadas)
        #self.mostrarCampo(self.campoMinado)

    def __repr__(self): 
        return f'matriz : {self.campoMinado}'

    def criar(self, nColuna, nLinha, nBombas):
        self.campo = [[' ' for i in range(nColuna)] for i in range(nLinha)]
        self.campoMinado = self.gerarBombas(self.campo, nBombas, nLinha, nColuna)
        self.nJogadas = nColuna * nLinha - nBombas
        return self.campoMinado

        #gera as bombas randomicamente
    def gerarBombas(self, campo, nBombas, nLinha, nColuna):
        nBombas = nBombas
        campoMinado = campo
        while nBombas > 0:
            x = random.randint(0, nLinha - 1)
            y = random.randint(0, nColuna - 1) 
            #print(x, y)
            for i in campo:
                if(campo[x][y] == 9):
                    continue
                else:
                    campo[x][y] = 9
                    nBombas = nBombas - 1
        return campoMinado

    def jogada(self, campoLimpo, campoMinado, nJogadas):
        
        self.totalJogadas = self.nJogadas
        while (self.nJogadas > 0):
            print('--> Você tem', self.nJogadas,'/', self.totalJogadas, 'jogadas restantes', '\n')
            self.linha = int(input("--> Informe a linha: "))
            self.coluna = int(input("--> Informe a coluna: "))

            #persistencia.Salvar(self.linha, self.coluna, self.nJogadas, campoMinado)

            if(type(campoLimpo[self.linha][self.coluna]) == str):     #compara se a area é diferente do codigo ascii do ' '
                if(campoMinado[self.linha][self.coluna] == 9):
                    print('BOMBA, GAME OVER!')
                    self.mostrarCampo(campoMinado)
                    break      
                else:
                    self.nJogadas = self.nJogadas - 1
                    self.vizinhos = self.pegaVizinhos(campoLimpo, campoMinado, self.linha, self.coluna)
                    print(self.vizinhos)
                    
                    campoLimpo, campoMinado = self.contaBombas(self.vizinhos, campoMinado, campoLimpo)
                    self.mostrarCampo(campoMinado)
                    self.mostrarCampo(campoLimpo)
            else:
                print('Jogada inválida, área já descoberta!', '\n')

    def pegaVizinhos(self, campoLimpo, campoMinado, linha, coluna):
        self.vizinhos = []
        #self.cont = 0
        for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            self.vizinhos.append((self.linha + i, self.coluna + j))
                            continue
                        #elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                            #erro na chamada recursiva, computador não suporta a qtd de chamadas
                            #self.vizinhoL = self.linha + i
                            #self.vizinhoC = self.coluna + j
                            #self.bombasVizinhas(campoMinado, self.vizinhoL, self.vizinhoC)
                            #self.cont += 1
                        elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] != 9:# and type(campoMinado[self.linha + i][self.coluna + j]) == str:
                            #self.pegaVizinhos(campoLimpo, campoMinado, self.linha + i, self.coluna + j)
                            self.vizinhos.append((self.linha + i, self.coluna + j))
                            #print(self.vizinhos)
                            
        #self.cont
        #self.campoLimpo[self.linha][self.coluna] = self.cont                            
        return self.vizinhos


    def contaBombas(self, vizinhos, campoMinado, campoLimpo):
        for x in self.vizinhos:
            self.linha = x[0]
            self.coluna = x[1]
            #self.vizinhos = self.pegaVizinhos(campoLimpo, campoMinado, self.x, self.y)
            #print(self.x, self.y)
            self.cont = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (self.linha + i) < len(campoMinado) and -1 < (self.coluna + j) < len(campoMinado) and campoMinado[self.linha + i][self.coluna + j] == 9:
                        self.cont += 1
            campoLimpo[self.linha][self.coluna] = self.cont                   
                        
            #self.campoLimpo[self.linha][self.coluna] = self.cont
            
            
        return campoLimpo, campoMinado          
    
    def mostrarCampo(self, campoAtual):
                print('================Início================', '\n')
                for linha in campoAtual:
                    print(end=' | ')
                    
                    for coluna in linha:
                        print(coluna, end=' | ')
                        self.fim = '--' * len(linha) * 2
                    print('\n', self.fim)
                print('\n', '================Fim================', '\n')

'''
        #mostra o campo com os índices
    def mostrarCampo(self, campoAtual):
        tamCampo = len(campoAtual)
        horizontal = '   ' + (4 * tamCampo * '-') + '-'
        superior = '     '

        for i in ascii_lowercase[:tamCampo]:
            superior = superior + i + '   '
        print(superior + '\n' + horizontal)

        for idx, i in enumerate(campoAtual):
            linha = '{0:2} |'.format(idx + 1)
            for j in i:
                linha = linha + ' ' + j + ' |'
            print(linha + '\n' + horizontal)
        print('')
'''

    
