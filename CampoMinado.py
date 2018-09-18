import random

class CampoMinado:

    def __init__(self, tamanho, numeroMinas):
        self.tamanho = tamanho
        self.numeroMinas = numeroMinas
        self.mina = self.configurarMina()
    
    def __len__(self):
      return self.tamanho

    def obterMina(self):
        return self.mina

    def carregarMina(self, minaSalva):
        self.mina = minaSalva

    def configurarMina(self):
        mina = [[' ' for i in range(self.tamanho)] for i in range(self.tamanho)]

        for i in range(self.numeroMinas):
            x, y = self.obterCampoRandom()
            mina[x][y] = 'X'
        return mina

    def clicarNaMina(self, coluna, linha):
        celula = self.mina[linha][coluna]
        if(celula == "X"):
            return "X"
        else:
            self.mina[linha][coluna] = "0" 
            return "0"

    def obterCampoRandom(self):        
        x = random.randint(0, self.tamanho-1)
        y = random.randint(0, self.tamanho-1)
        return (x,y)
    
    