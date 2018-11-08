from random import randint
import rpyc
from rpyc.utils.server import ThreadedServer
import sys

class CampoMinadoServer(rpyc.Service):

    COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
    GAME_OVER = "Game Over"

    def criar_novo_jogo(self, linha, coluna):
        self.__linha = linha
        self.__coluna = coluna
        self.jogadas_restantes = self.__calcular_total_jogadas(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)

    def efetuar_jogada(self, linha, coluna):
        if not self.__validar_coordenadas(linha, coluna):
            return self.COORDENADAS_INVALIDAS
        if  (linha, coluna) in self.__coordenadas_bombas:
            return self.GAME_OVER

        self.jogadas_restantes -=1
        return str(self.__conta_bombas_vizinhos(linha, coluna))

    def get_jogadas_restantes(self):
        return self.jogadas_restantes
    
    def jogo_incompleto(self):
        return False

    def __preparar_jogada(self, text):
        jogada = text.split(".")
        return int(jogada[0]), int(jogada[1])

    def __distribuir_bombas(self, linha, coluna):
        coordenadas_bombas = [(randint(0, linha - 1), randint(0, coluna - 1)) for x in range(self.__total_bombas())]
        print(coordenadas_bombas)
        return coordenadas_bombas

    def __total_bombas(self):
        return int((self.__linha*self.__coluna)/3)
    
    def __calcular_total_jogadas(self,linha, coluna):
        return (linha*coluna) - self.__total_bombas()

    def __validar_coordenadas(self, linha, coluna):
        if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
            return True
        return False
    
    def __coordenada_e_bomba(self, coordenada):
        return coordenada in self.__coordenadas_bombas

    def __conta_bombas_vizinhos(self, linha, coluna):
        return len([(linha + x, coluna + y) for x in (-1,0,1) for y in (-1,0,1) if self.__coordenada_e_bomba((linha + x, coluna + y))])

if __name__ == "__main__":
    try:
        print("servidor iniciado")
        thread = ThreadedServer(CampoMinadoServer, port=18861)
        thread.start() 
    except:
        for val in sys.exc_info():
            print(val)