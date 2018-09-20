from numpy import * 
from os import system, name 
from time import sleep 

class CampoMinado:
	
	lugaresEscolhidos = []
	tamanho = 0
	numBombas = 0
	totalJogadas = 0

	def clear(): 
		if name == 'nt': 
			_ = system('cls') 

		else: 
			_ = system('clear') 

	def setaTamanhoCampoMinado(self,nivel):
		if(nivel == "1"):
			self.tamanho = 5
			self.numBombas = 5
			self.totalJogadas = 5
			
		elif(nivel == "2"):
			self.tamanho = 10
			self.numBombas = 25
			self.totalJogadas = 10
			
		elif(nivel == "3"):
			self.tamanho = 15
			self.numBombas = 70
			self.totalJogadas = 15
		
		self.tabuleiro = [[0 for x in range(self.tamanho)] for y in range(self.tamanho)]
		self.tabuleiroExibicao = [[0 for x in range(self.tamanho)] for y in range(self.tamanho)]


	def posicionaBombas(self):
		numBombas = 0
		while(numBombas < self.numBombas):
			x = random.choice(self.tamanho-1)
			y = random.choice(self.tamanho-1)
			if(self.tabuleiro[x][y] == False):
				self.tabuleiro[x][y] = True
				numBombas += 1

	def inicializaMatriz(self):
		for i in range(self.tamanho):
			for j in range(self.tamanho):
				self.tabuleiroExibicao[i][j] = "_"
		self.posicionaBombas()
	
	def printaTabelaExibicao(self):
		for i in range(self.tamanho):
			for j in range(self.tamanho):
				print(self.tabuleiroExibicao[i][j], end=' ')
			print("\n")
	
	def printaGabarito(self):
		for i in range(self.tamanho):
			for j in range(self.tamanho):
				print(self.tabuleiro[i][j], end=' ')
			print("\n")

	def printaCampo(self):
		for i in range(self.tamanho):
			for j in range(self.tamanho):
				print(self.tabuleiro[i][j])
	
	def calculaQntBombasAoRedor(self,x,y):
		qntBombas = 0
		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				if (i < self.tamanho and i > -1) and (j < self.tamanho and j > -1):
					
					if self.tabuleiro[i][j] == True:
						qntBombas = qntBombas + 1
		return qntBombas		

	def escolheArea(self):
		print("Escolha um território no Campo. Informe as coordenadas:")
		x=int(input("x="))
		y=int(input("y="))
		place = [x,y]
		print(place)
		print(self.lugaresEscolhidos)
		if [(x,y)] in self.lugaresEscolhidos:
			print("você ja escolheu essa regiao")
		else:
			if self.tabuleiro[x][y] == True:
				self.lugaresEscolhidos.append([x,y])
				print(self.lugaresEscolhidos)
				self.tabuleiroExibicao[x][y] = '*'
				return False
			else:
				self.lugaresEscolhidos.append([x,y])
				print(self.lugaresEscolhidos)
				self.tabuleiroExibicao[x][y] = self.calculaQntBombasAoRedor(x,y)
				return True
	
