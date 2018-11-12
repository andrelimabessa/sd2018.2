import clienteModelo

class CampoMinado(clienteModelo.CampoMinado):                                                                                
    
    def __init__(self, fieldSize):                                                     
        super().__init__(fieldSize)                                                     

    def showCleanField(self):

        self.close = '--' * len(self.cleanField) * 2                                     
        print('\n', '', self.close)                                                     
        for line in self.cleanField:                                                    
            print(end=' | ')                                                           
            for column in line:
                print(column, end=' | ')
            print('\n', '', self.close)                                                 

    def updateDict(self, answer):

        x = -1
        sizeField = range(len(self.cleanField))
        for l in sizeField:                                                            
            y = 0
            x = x + 1
            for c in sizeField:
                self.cleanField[x][y] = answer[(x, y)]                                         
                y = y + 1

    def translateReturn(self, answer):

        if(answer['altered'] == True):                                                  
            self.updateDict(answer)                                                     
            self.showCleanField()                                                       
            self.dict['played'] = self.dict['played'] + 1                               
            print(answer['msg'])                                                        
            print('Ainda não descobriu ', answer['freeAreas'], 'áreas')                       

        else:                                                                           
            self.showCleanField()                                                       
            print(answer['msg'])                                                        
            print('Ainda não descobriu ', answer['freeAreas'], 'áreas')                       

        if(answer['freeAreas'] == 0):                                                   
            print('Você ganhou!')                                              

