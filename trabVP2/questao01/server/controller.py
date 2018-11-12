import domain

class Minefield(domain.Field):
    def __init__(self, size, bombs):
        super().__init__(size, bombs)            

    def bombCount(self, neighbors):
        for x in self.neighbors:
            self.line = x[0]
            self.column = x[1]
            self.count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (self.line + i) < len(self.mineField) and -1 < (self.column + j) < len(self.mineField) and self.mineField[self.line + i][self.column + j] == 9:
                        self.count += 1
            self.cleanField[self.line][self.column] = self.count

    def countFreeArea(self):
        self.count = 0
        sizeField = len(self.cleanField)
        for line in range(0, sizeField):
            for column in range(0, sizeField):
                if (type(self.cleanField[line][column]) == str):
                    self.count = self.count + 1
        print(self.count, self.numberBomb)
        print('Áreas livre:', self.count - self.numberBomb)
        return self.count - self.numberBomb
        
    def played(self, line, column):
        if(line > (len(self.cleanField) - 1) or column > (len(self.cleanField) - 1) or line < 0 or column < 0):
            self.dict['controlPlay'] = 1
            self.dict['msg'] = 'Jogada inválida!'
            self.dict['altered'] = False
        
        elif(self.mineField[line][column] == 9):
            self.dict['controlPlay'] = 2
            self.dict['msg'] = 'Bomba, Fim de Jogo!'
            self.mineField = self.updateDict(self.mineField)

        elif(type(self.cleanField[line][column]) == str):  
            neighbors = self.takeNeighbors(line, column)
            self.bombCount(neighbors)
            self.dict['controlPlay'] = 3
            self.dict['msg'] = 'Jogada de sucesso!'
            self.dict['played'] += 1
            self.dict['freeAreas'] = self.countFreeArea()
            self.cleanField = self.updateDict(self.cleanField)
        
        else:
            self.dict['controlPlay'] = 4
            self.dict['msg'] = 'Área já descoberta'
            self.dict['altered'] = False
            

    def takeNeighbors(self, line, column):
        self.neighbors = []
        #self.cont = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    
                    self.neighbors.append((line + i, column + j))
                    continue
                elif -1 < (line + i) < len(self.mineField) and -1 < (column + j) < len(self.mineField) and self.mineField[line + i][column + j] != 9:
                    self.neighbors.append((line + i, column + j))
        return self.neighbors
    
    def updateDict(self, field):
        x = -1
        sizeField = range(len(field))
        for l in sizeField:
            y = 0
            x = x + 1
            for c in sizeField:
                self.dict[(x, y)] = field[x][y]               
                y = y + 1
        self.dict['altered'] = True
        if (self.dict['freeAreas'] <= 0):
            self.dict['msg'] = 'Você ganhou!'
        return field
        

    def showMineField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.mineField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
            print('\n', '', self.close)
                    

    def showCleanField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.cleanField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
            print('\n', '', self.close)        