import servidorModelo


class CampoMinado(servidorModelo.Campo):
    def __init__(self, fieldSize, numberBomb, mineField):
        super().__init__(fieldSize, numberBomb)
        self.alimentarMineField()
        
    def showMineField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.mineField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
                #self.close = '--' * len(line) * 2
            print('\n', '', self.close)
                    

    def showCleanField(self):
        print('\n')
        self.close = '--' * len(self.mineField) * 2
        print('\n', '', self.close)
        for line in self.cleanField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
                #self.close = '--' * len(line) * 2
            print('\n', '', self.close)        


    def alimentarMineField(self):
        x = -1
        sizeField = self.cleanField
        for l in sizeField:
            y = 0
            x = x + 1
            for c in sizeField:
                self.dictMineField[(x, y)] = self.mineField[x][y]          
                y = y + 1


class Game():
    def __init__(self, data, campoLimpo, campoMinado):

        self.data = data
        self.campoLimpo = campoLimpo
        self.campoMinado = campoMinado
        self.cleanField = [['-' for i in
        range(data['sizeField'])] for i in range(data['sizeField'])]
        self.mineField = [[0 for i in
        range(data['sizeField'])] for i in range(data['sizeField'])]
        self.alimentarCampoLimpo()
        self.alimentarCampoMinado()
        self.dict = self.createDictionary({}, data['sizeField'])
        self.played(data['line'], data['column'])
    
    def createDictionary(self, dict, sizeField):

        for x in range(sizeField):
            for y in range(sizeField):
                dict[(x, y)] = '-'

        dict['msg'] = 'Inicio'
        dict['freeAreas'] = (sizeField * sizeField - self.data['numberBomb'])
        dict['played'] = 0
        dict['altered'] = True
        dict['contolPlay'] = 0
        return dict

    def alimentarCampoLimpo(self):
       

        for l in range(len(self.cleanField)):
            for c in range(len(self.cleanField)):
                self.cleanField[l][c] = self.campoLimpo[(l, c)]          
                c = c + 1
            l = l + 1

    def alimentarCampoMinado(self):
        for l in range(len(self.cleanField)):
            for c in range(len(self.cleanField)):
                self.mineField[l][c] = self.campoMinado[(l, c)]          
                c = c + 1
            l = l + 1

    def played(self, line, column):
        if(line > (len(self.cleanField) - 1) or column > (len(self.cleanField) - 1) or line < 0 or column < 0):
            self.dict['controlPlay'] = 1
            self.dict['msg'] = 'Jogada inválida, coordenadas não existem para esse campo!'
            self.dict['altered'] = False
        
        elif(self.campoMinado[(line, column)] == 9):
            self.dict['controlPlay'] = 2
            self.dict['msg'] = 'Game Over!'
            self.updateDict()

        elif(self.campoMinado[(line, column)] == '-'):  
            neighbors = self.takeNeighbors(line, column)
            self.bombCount(neighbors)
            self.dict['controlPlay'] = 3
            self.dict['msg'] = 'Boa jogada!'
            self.dict['played'] += 1
            self.dict['freeAreas'] = self.countFreeArea()
            self.updateDict()
        
        else:
            self.dict['controlPlay'] = 4
            self.dict['msg'] = 'Jogada inválida, já foi usada anteriormente'
            self.dict['altered'] = False
            

    def takeNeighbors(self, line, column):
        self.neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    
                    self.neighbors.append((line + i, column + j))
                    continue
                elif -1 < (line + i) < len(self.mineField) and -1 < (column + j) < len(self.mineField) and self.mineField[line + i][column + j] != 9:
                    self.neighbors.append((line + i, column + j))
                         
        return self.neighbors


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
        
        return self.count - self.data['numberBomb']

    
    def updateDict(self):
        for l in range(len(self.cleanField)):
            for c in range(len(self.cleanField)):
                self.dict[(l, c)] = self.mineField[l][c]               
                c = c + 1
        l = l + 1
        self.dict['altered'] = True
        if (self.dict['freeAreas'] <= 0):
            self.dict['msg'] = 'Você ganhou!'   

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
        

        


        
        