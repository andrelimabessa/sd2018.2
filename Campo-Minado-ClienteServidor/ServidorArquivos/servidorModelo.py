import random

class Campo:
    
    def __init__(self, fieldSize, numberBomb):
        self.numberBomb = numberBomb
        self.cleanField = [['-' for i in range(fieldSize)] for i in range(fieldSize)] 
        self.mineField = self.generateBomb([['-' for i in range(fieldSize)] for i in range(fieldSize)], 
                                                self.numberBomb)
        self.dict = self.createDictionary({}, self.cleanField)
    

    def generateBomb(self, cleanField, numberBomb):
        numberBomb = numberBomb
        fieldSize = len(cleanField)
        mineField = cleanField
        while numberBomb > 0:
            x = random.randint(0, fieldSize - 1)
            y = random.randint(0, fieldSize - 1) 
            for i in mineField:
                if(mineField[x][y] == 9):
                    continue
                else:
                    mineField[x][y] = 9
                    numberBomb = numberBomb - 1
        return mineField


    def createDictionary(self, dict, cleanField):
        fieldSize = len(cleanField)
        for x in range(fieldSize):
            for y in range(fieldSize):
                dict[(x, y)] = '-'
        return dict


if __name__ == '__main__':
    cm = Campo(3, 3)
    print(cm.cleanField)
    print(cm.mineField)
    print(cm.dict)
    print(cm.numberBomb)
    print(type(cm.dict))
    a = str(cm.dict)
    print(a)
    print(type(a))