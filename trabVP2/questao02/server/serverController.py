import serverModel

class MineField(serverModel.Campo):                                                                                   
    def __init__(self, fieldSize, numberBomb):                                                                             
        super().__init__(fieldSize, numberBomb)                                                                            
        
    def played(self, line, column):
        if(line > (len(self.cleanField) - 1) or column > (len(self.cleanField) - 1) or line < 0 or column < 0):            
            self.dict['controlPlay'] = 1                                                                                  
            self.dict['msg'] = 'Jogada inválida!'
            self.dict['altered'] = False                                                                                  
        elif(self.mineField[line][column] == 9):                                                                           
            self.dict['controlPlay'] = 2                                                                                   
            self.dict['msg'] = 'Bomba, Final de Jogo!'
            self.dict['altered'] = True  
            self.updateDict(self.mineField)                                                                               
        elif(type(self.cleanField[line][column]) == str):                                                                  
            neighbors = self.takeNeighbors(line, column)                                                                   
            self.bombCount(neighbors)                                                                                      
            self.dict['controlPlay'] = 3                                                                                  
            self.dict['msg'] = 'Jogada de sucesso!'
            self.dict['played'] += 1
            self.dict['altered'] = True                                                                                    
            self.dict['freeAreas'] = self.countFreeArea()                                                                  
            self.updateDict(self.cleanField)                                                                              
        else:                                                                                                              
            self.dict['controlPlay'] = 4                                                                                   
            self.dict['msg'] = 'Área já descoberta'
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
        return self.count - self.numberBomb                                           

    
    def updateDict(self, field):
        x = -1
        sizeField = range(len(field))                                                
        for l in sizeField:                                                          
            y = 0
            x = x + 1
            for c in sizeField:
                self.dict[(x, y)] = field[x][y]                                                   
                y = y + 1        

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
        