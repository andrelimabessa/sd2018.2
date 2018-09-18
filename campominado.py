from random import randint
from os.path import isfile
from os import remove
import json

class CampoMinado:

    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.total_jogadas = (linha * coluna) - self.totalBombas(linha, coluna)
        self.tabuleiro = self.iniciaTabuleiro(linha, coluna)
        self.coordenadas_bombas = self.distribuiBombas(linha,coluna)

    def totalBombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def iniciaTabuleiro(self, linha, coluna):
        return [['*' for x in range(coluna)] for j in range(linha)]

    def distribuiBombas(self, linha, coluna):
        quantidade_bombas = self.totalBombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        return coordenadas_bombas

    def imprimirTabuleiro(self):
        for posicao in self.tabuleiro:
            print(str(posicao))

    def validaCordenadas(self, linha, coluna):
        if linha not in range(0, self.linha):
            print("linha inválida")
            return False
        elif coluna not in range(0, self.coluna):
            print("coluna inválida")
            return False
        return True

    def contaBombasVizinho(self, linha, coluna):
        bombas = 0
        for line in range(linha-1, linha+1):
            for col in range(coluna-1, coluna+1):
                posicao = (line, col)
                if posicao in self.coordenadas_bombas:
                    bombas += 1
        return str(bombas)

    def marcaJogada(self, linha, coluna):
        marcador = self.contaBombasVizinho(linha, coluna)
        self.tabuleiro[linha][coluna] = marcador
        self.imprimirTabuleiro()

    def proximaJogada(self):
        return self.total_jogadas > 0

    def gameOver(self):
        print("------------------------GAME OVER--------------------")
        remove("game.json")

    def jogada(self, linha, coluna):
        if self.validaCordenadas(linha, coluna):
            posicao = (linha, coluna)
            if posicao in self.coordenadas_bombas:
                self.imprimirTabuleiro()
                self.total_jogadas = 0
                self.gameOver()
            else:
                self.marcaJogada(linha, coluna)
                self.total_jogadas -= 1
                print("Jogadas restantes: " + str(self.total_jogadas))
                self.salvar()

                if self.total_jogadas == 0:
                    print("Jogo finalizado, parabéns!")
                    remove("game.json")

    def salvar(self):

        salva = {
            'linha': self.linha,
            'coluna': self.coluna,
            'total_jogadas': self.total_jogadas,
            'tabuleiro': self.tabuleiro,
            'coordenadas_bombas': self.coordenadas_bombas
        }
        arquivo = open("salva.json", 'w')

        arquivo.write(json.dumps(salva))
        arquivo.close()

    def restaurar(self, salva):
        self.linha = salva['linha']
        self.coluna = salva['coluna']
        self.total_jogadas = salva['total_jogadas']
        self.tabuleiro = salva['tabuleiro']
        self.coordenadas_bombas = salva['coordenadas_bombas']