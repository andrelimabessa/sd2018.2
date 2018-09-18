from random import randint

class CampoMinado():

    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.total_bombas = 5
        self.total_jogadas = self.linhas * self.colunas - self.total_bombas
        self.bombas = self.criar_bombas()
        self.jogadas = []

    def criar_bombas(self):
        lista = []

        for _ in range(self.total_bombas):
            continuar = True
            while continuar:
                bomba = (randint(0, self.linhas), randint(0, self.colunas))
                if bomba not in lista:
                    lista.append(bomba)
                    continuar = False
        return lista

    def jogada(self, linha, coluna):
        self.jogadas.append((linha, coluna))
