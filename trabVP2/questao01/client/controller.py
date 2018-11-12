import domain

class Minefield(domain.Field):
    def __init__(self, fieldSize):
        super().__init__(fieldSize)

    def showCleanField(self):
        print('\n')
        self.close = '--' * len(self.cleanField) * 2
        print('\n', '', self.close)
        for line in self.cleanField:
            print(end=' | ')
            for column in line:
                print(column, end=' | ')
                #self.close = '--' * len(line) * 2
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
