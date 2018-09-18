from random import randint
from os.path import isfile
from os import remove
import json

class CampoMinado:

    def __init__(self, linha, coluna):
        
        self.linha = linha
        self.coluna = coluna
        self.jogadas_totais = (linha * coluna) - self.bombas_totais(linha, coluna)
        self.tabuleiro = self.iniciar_tabuleiro(linha, coluna)
        self.posicao_bombas = self.posicionar_bombas(linha,coluna)

    def iniciar_tabuleiro(self, linha, coluna):
        return [['x' for x in range(1,coluna)] for j in range(1,linha)]

    def posicionar_bombas(self, linha, coluna):
        qtd_bombas = self.bombas_totais(linha, coluna)
        posicao_bombas = []
        while qtd_bombas > 0:
            posicoes = (randint(0, linha - 1), randint(0, coluna - 1))
            if posicoes not in posicao_bombas:
                posicao_bombas.append(posicoes)
                qtd_bombas-=1
        return posicao_bombas

    def bombas_totais(self, linha, coluna):
        return int((linha*coluna)/2)

    def mostrar_tabuleiro(self):
        for posicao in self.tabuleiro:
            print(str(posicao))

    def posicoes_validas(self, linha, coluna):
        if linha not in range(0, self.linha):
            if not linha:
                print("linha invalida")
                return False
        elif coluna not in range(0, self.coluna):
            if not coluna:
                print("coluna invalida")
                return False
        return True

    def bombas_vizinhas(self, linha, coluna):
        bombas = 0
        for line in range(linha-1, linha+1):
            for col in range(coluna-1, coluna+1):
                posicao = (line, col)
                if posicao in self.posicao_bombas:
                    bombas += 1
        return str(bombas)

    def marca_jogada(self, linha, coluna):
        marcador = self.bombas_vizinhas(linha, coluna)
        self.tabuleiro[linha][coluna] = marcador
        self.mostrar_tabuleiro()

    def proxima_jogada(self):
        return self.jogadas_totais > 0

    def fimDoJogo(self):
        print("***********************************************")
        print("______________YOU WON__________________________")
        print("*******************************************\n\n")
        remove("jogo.json")

    def jogada(self, linha, coluna):
        if self.posicoes_validas(linha, coluna):
            posicao = (linha, coluna)
            if posicao in self.posicao_bombas:
                self.mostrar_tabuleiro()
                self.jogadas_totais = 0
                self.fimDoJogo()
            else:
                self.marca_jogada(linha, coluna)
                self.jogadas_totais -= 1
                print("Faltam " + str(self.jogadas_totais) + "jogadas")
                self.salvar_jogo_corrente()

                if self.jogadas_totais == 0:
                    print("***********************************************")
                    print("______________YOU WIN__________________________")
                    print("*******************************************\n\n")
                    remove("jogo.json")


    #Salva o jogo corrente escrevendo as informações no arquivo json
    def salvar_jogo_corrente(self):

        jogo = {
            'linha': self.linha,
            'coluna': self.coluna,
            'jogadas_totais': self.jogadas_totais,
            'tabuleiro': self.tabuleiro,
            'posicao_bombas': self.posicao_bombas
        }
        arquivo = open("jogo.json", 'w')

        arquivo.write(json.dumps(jogo))
        arquivo.close()

    #Restaura o jogo corrente coletando as informações do arquivo json
    def restaurar(self, jogo):
        self.linha = jogo['linha']
        self.coluna = jogo['coluna']
        self.jogadas_totais = jogo['jogadas_totais']
        self.tabuleiro = jogo['tabuleiro']
        self.posicao_bombas = jogo['posicao_bombas']
