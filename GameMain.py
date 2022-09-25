from auxiliares import *
from Board import *

class GameMain():
	
	#Constructor to setup the game
	def __init__(self):
		#Perform one-time initialization tasks
		self.initGame()
		#Reset the board, currentStatus and currentPlayer
		self.newGame()
		#Play the game once                
		while True:   				         
			#The currentPlayer makes a move.
			#Update cells[][] and currentState
			self.stepGame()
			#Refresh the display
			self.board.paint()
			#Print message if game over
			if self.currentState == State.CROSS_WON:
				print("'X' won!\nBye!")
			elif self.currentState == State.NOUGHT_WON:
				print("'O' won!\nBye!")
			elif self.currentState == State.DRAW:
				print("It's Draw!\nBye!")	
			#Switch currentPlayer
			self.currentPlayer = Seed.NOUGHT if self.currentPlayer == Seed.CROSS else Seed.CROSS
			if self.currentState != State.PLAYING:
				break

	#Perform one-time initialization tasks 
	def initGame(self):
		self.board = Board() # allocate game-board	

	#Reset the game-board contents and the current states, ready for new game
	def newGame(self):
		self.board.newGame() 			#clear the board contents		
		print("Who starts?\n 1. Player\t2. PC")    		
		self.initPlayer = int(input("Choose a number > "))
		self.currentPlayer = Seed.CROSS 		# CROSS plays first
		self.currentState = State.PLAYING 	# ready to play
		self.turno = 1
		

	
	#The currentPlayer makes one move. Update cells[][] and currentState.	
	def stepGame(self):
		#turno del usuario		
		if ((self.currentPlayer == Seed.CROSS and self.initPlayer == 1)
			or (self.currentPlayer == Seed.NOUGHT and self.initPlayer == 2)):
			validInput = False # for validating input
			while True:								
				print("Player {0}, enter your move (row[1-3] column[1-3]): ".format(self.currentPlayer))
				row = int(input("row:")) - 1 # [0-2]
				col = int(input("col:")) - 1
				if (row >= 0 and row < self.board.ROWS and col >= 0 and col < self.board.COLS
						and self.board.cells[row][col].content == Seed.NO_SEED):
					#Update cells[][] and return the new game state after the move
					self.currentState = self.board.stepGame(self.currentPlayer, row, col)
					validInput = True # input okay, exit loop
				else:
					print("This move at ({} {}) is not valid. Try again...".format(row + 1,col+1))				
				if validInput == True: # repeat until input is valid
					break
		else:  # Turnos pares (computadora)
			print("My turn...")
			if self.turno == 1:
				#impares = X pares= O			
				self.currentState = self.board.stepGame(self.currentPlayer, 0, 0) # go(1)						
			elif self.turno == 2:
				if self.board.cells[1][1].content == Seed.NO_SEED:
					self.currentState = self.board.stepGame(self.currentPlayer, 1, 1) # go(5)
				else:
					self.currentState = self.board.stepGame(self.currentPlayer, 0, 0) # go(1)				
			elif self.turno == 3:
				if self.board.cells[2][2].content == Seed.NO_SEED:
					self.currentState = self.board.stepGame(self.currentPlayer, 2, 2) #go(9)
				else:
					self.currentState = self.board.stepGame(self.currentPlayer, 0, 2) # go(3)			
			elif self.turno == 4:				
				if self.possWin(Seed.CROSS) != None:
					cell = self.possWin(Seed.CROSS)  # bloquear oponente
				else:
					cell = self.make2()
				self.currentState = self.board.stepGame(self.currentPlayer, cell[0], cell[1])				
			elif self.turno == 5:
				cell = [ 0, 2 ] # go(3)
				if self.possWin(Seed.CROSS) != None: # ganar
					cell = self.possWin(Seed.CROSS)
				elif self.possWin(Seed.NOUGHT) != None:
					cell = self.possWin(Seed.NOUGHT)	# bloquear
				elif self.board.cells[2][0].content == Seed.NO_SEED: # go(7)				
					cell[0] = 2
					cell[1] = 0				
				self.currentState = self.board.stepGame(self.currentPlayer, cell[0], cell[1])						
			elif self.turno == 6:				
				if self.possWin(Seed.NOUGHT) != None:
					cell = self.possWin(Seed.NOUGHT)
				elif self.possWin(Seed.CROSS) != None:
					cell = self.possWin(Seed.CROSS)
				else:
					cell = self.make2()
				self.currentState = self.board.stepGame(self.currentPlayer, cell[0], cell[1])
			elif self.turno == 7 or self.turno == 9:					
				if self.possWin(Seed.CROSS) != None:
					cell = self.possWin(Seed.CROSS)
				elif self.possWin(Seed.NOUGHT) != None:
					cell = self.possWin(Seed.NOUGHT)
				elif self.make2() != None:
					cell = self.make2()
				else:
					#buscar celda vacia
					cell = self.searchEmptyCell()					
				self.currentState = self.board.stepGame(self.currentPlayer, cell[0], cell[1])
			elif self.turno == 8:				
				if self.possWin(Seed.NOUGHT) != None:
					cell = self.possWin(Seed.NOUGHT)
				elif self.possWin(Seed.CROSS) != None:
					cell = self.possWin(Seed.CROSS)
				elif self.make2() != None:
					cell = self.make2()
				else:
					cell = self.searchEmptyCell()				
				self.currentState = self.board.stepGame(self.currentPlayer, cell[0], cell[1])				
		self.turno += 1

	def make2(self):
		cell = [-1, -1]
		# checar si el centro esta vacio
		if self.board.cells[1][1].content == Seed.NO_SEED:
			cell[0] = 2
			cell[1] = 2
			return cell
		else:
			#Trampa de flecha
			if (self.board.cells[1][1].content == Seed.CROSS 
				and self.board.cells[2][2].content == Seed.CROSS
				and self.board.cells[0][2].content == Seed.NO_SEED):
				cell[0] = 0
				cell[1] = 2
				return cell
			#buscar celda que no es esquina y este vacia
			if self.board.cells[0][1].content == Seed.NO_SEED:
				cell[0] = 0
				cell[1] = 1
				return cell
			elif self.board.cells[1][0].content == Seed.NO_SEED:
				cell[0] = 1
				cell[1] = 0
				return cell
			elif self.board.cells[1][2].content == Seed.NO_SEED:
				cell[0] = 1
				cell[1] = 2
				return cell
			elif self.board.cells[2][1].content == Seed.NO_SEED:
				cell[0] = 2
				cell[1] = 1
				return cell			
			return None		
	
	def possWin(self, player):
		#3-in-the-row
		cell = [-1, -1 ]
		for i in range(3):
			if (self.board.cells[i][0].content == player and self.board.cells[i][1].content == player
					and self.board.cells[i][2].content == Seed.NO_SEED):
				cell[0] = i
				cell[1] = 2
				return cell
			elif (self.board.cells[i][0].content == player and self.board.cells[i][1].content == Seed.NO_SEED
					and self.board.cells[i][2].content == player):
				cell[0] = i
				cell[1] = 1
				return cell
			elif (self.board.cells[i][0].content == Seed.NO_SEED and self.board.cells[i][1].content == player
					and self.board.cells[i][2].content == player):
				cell[0] = i
				cell[1] = 0
				return cell

		# 3-in-the-column
		for i in range(3): 
			if (self.board.cells[0][i].content == player and self.board.cells[1][i].content == player
					and self.board.cells[2][i].content == Seed.NO_SEED):
				cell[0] = 2
				cell[1] = i
				return cell
			elif (self.board.cells[0][i].content == player and self.board.cells[1][i].content == Seed.NO_SEED
					and self.board.cells[2][i].content == player):
				cell[0] = 1
				cell[1] = i
				return cell
			elif (self.board.cells[0][i].content == Seed.NO_SEED and self.board.cells[1][i].content == player
					and self.board.cells[2][i].content == player):
				cell[0] = 0
				cell[1] = i
				return cell
		# 3-in-the-diagonal
		if (self.board.cells[0][0].content == player and self.board.cells[1][1].content == player
				and self.board.cells[2][2].content == Seed.NO_SEED):
			cell[0] = 2
			cell[1] = 2
			return cell
		elif (self.board.cells[0][0].content == player and self.board.cells[1][1].content == Seed.NO_SEED
				and self.board.cells[2][2].content == player):
			cell[0] = 1
			cell[1] = 1
			return cell
		elif (self.board.cells[0][0].content == Seed.NO_SEED and self.board.cells[1][1].content == player
				and self.board.cells[2][2].content == player):
			cell[0] = 0
			cell[1] = 0
			return cell		
		# 3-in-the-opposite-diagonal
		if (self.board.cells[0][2].content == player and self.board.cells[1][1].content == player
				and self.board.cells[2][0].content == Seed.NO_SEED):
			cell[0] = 2
			cell[1] = 0
			return cell
		elif (self.board.cells[0][2].content == player and self.board.cells[1][1].content == Seed.NO_SEED
				and self.board.cells[2][0].content == player):
			cell[0] = 1
			cell[1] = 1
			return cell
		elif (self.board.cells[0][2].content == Seed.NO_SEED and self.board.cells[1][1].content == player
				and self.board.cells[2][0].content == player):
			cell[0] = 0
			cell[1] = 2
			return cell		
		return None
	
	def searchEmptyCell(self):	
		cell = None	
		for row in range(self.board.ROWS):
			for col in range(self.board.COLS):
				if self.board.cells[row][col].content == Seed.NO_SEED:
					cell[0] = row
					cell[1] = col
		return cell


GameMain() # Let the constructor do the job	