from auxiliares import Seed

class Cell():
    
    def __init__(self, row, col):
        self.row = row        
        self.content = Seed.NO_SEED

    def newGame(self):
        self.content = Seed.NO_SEED
    
    def paint(self):
        print(self.content, end="")