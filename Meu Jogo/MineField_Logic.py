import random

class MineField:

    def __init__(self, size, numberOfMines):
        self.size = size
        self.numberOfMines = numberOfMines
        self.mine = self.configureMine()
    
    def getSize(self):
		return self.size
	
	def getRandomCell(self):
		return (random.randint(0, self.size-1),random.randint(0, self.size-1))
		
    def getMine(self):
        return self.mine

    def loadMine(self, mineSalva):
        self.mine = mineSalva

    def configureMine(self):
        mine = [[' ' for i in range(self.size)] for i in range(self.size)]

        for i in range(self.numberOfMines):
            x, y = self.obterCampoRandom()
            mine[x][y] = '#'
        return mine

    def getClick(self, column, row):
        cell = self.mine[row][column]
        if(cell != "#"):
            self.mine[row][column] = self.getNeighbours(column, row) 
            return self.getNeighbours(column, row)
        else:
			return "#"            

    def getNeighbours(self, column, row):
        numberOfMines = 0
        if self.mine[row][column + 1] == "#":  numberOfMines+=1
        if self.mine[row][column - 1] == "#": numberOfMines+=1
        if self.mine[row + 1][column] == "#": numberOfMines+=1
        if self.mine[row - 1][column] == "#": numberOfMines+=1
        if self.mine[row + 1][column + 1] == "#": numberOfMines+=1
        if self.mine[row - 1][column - 1] == "#": numberOfMines+=1
        if self.mine[row + 1][column - 1] == "#": numberOfMines+=1
        if self.mine[row - 1][column + 1] == "#": numberOfMines+=1
        return numberOfMines