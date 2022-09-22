
from Cell import Cell
from auxiliares import *

class Board():
    ROWS = 3
    COLS = 3
    cells = [[]]

    def __init__(self):
        self.initGame()
    
    def initGame(self):
        self.cells = [[Cell(row,col) for col in range(self.COLS)] 
                        for row in range(self.ROWS)]

    def newGame(self):        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.cells[row][col].newGame()

    def stepGame(self, player, selectedRow, selectedCol):
        #update game board
        self.cells[selectedRow][selectedCol].content = player

        if (self.cells[selectedRow][0].content == player            #3 en fila
                and self.cells[selectedRow][1].content == player    
                and self.cells[selectedRow][2].content == player    
            or  self.cells[0][selectedCol].content == player        #3 en columna
                and self.cells[1][selectedCol].content == player 
                and self.cells[2][selectedCol].content == player
            or  selectedRow == selectedCol                          #3 en diagonal
                and self.cells[0][0].content == player 
                and self.cells[1][1].content == player
                and self.cells[2][2].content == player
            or  selectedRow + selectedCol == 2                       #3 en diagonal inversa
                and self.cells[0][2].content == player 
                and self.cells[1][1].content == player
                and self.cells[2][0].content == player):            
                return State.CROSS_WON if player == Seed.CROSS else State.NOUGHT_WON
        else:
            #Buscar casilla disponible
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    if self.cells[row][col].content == Seed.NO_SEED:
                        return State.PLAYING
            return State.DRAW #es un empate



    def paint(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                print(" ", end="")
                self.cells[row][col].paint()
                print(" ", end="")
                if col < self.COLS - 1:
                    print("|", end="")
            print()
            if row < self.ROWS - 1:
                print("-----------")
        print()
