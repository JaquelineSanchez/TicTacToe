from enum import Enum

class Seed(Enum):

    CROSS = 'X'
    NOUGHT = 'O'
    NO_SEED = ' '

    def __str__(self):
        return self.value

class State(Enum):

    PLAYING = 1
    DRAW = 2
    CROSS_WON = 3
    NOUGHT_WON = 4

def validarNumero(min, max, mensaje):
    while True:
        valor = int(input(mensaje)) - 1
        if min <= valor <= max:
            return valor

