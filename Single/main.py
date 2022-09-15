###
# Takes too long and is linear.
###

from copy import deepcopy
numberswap=(
	 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
	'u', 'v', 'w', 'x', 'y', 'z', '.', '!', '¡', '?',
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
	'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
	'U', 'V', 'W', 'X', 'Y', 'Z')

# Start Function
def start():
	result= None
#	for x in range(4):
#		for y in range(4):
#			knight= Knight(x, y)
#			result= knight.test()
#			print(f"Test at ({x}, {y}) complete")
#
#			if result: break
#		if result: break

	result= Knight(0, 0).test()

	if result: Knight.printBoard(result)
	else: print("Not possible.")




# Knight Piece Class
class Knight:
	def __init__(self, x, y):
		self.boards= [ [ ['•' for _ in range(8)] for _ in range(8)] ]
		self.board= self.boards[0]
		self.x, self.y= x, y
		self.board[x][y]= '#'
		self.first= True


	# Moves Knigth Piece
	def makeMove(self, move):
		self.first= False
		x, y= self.x, self.y
		self.x, self.y= move
		self.board[self.x][self.y]= '$'
		self.boards.append(deepcopy(self.board) )
		z= len(self.boards)-1
		print(z)
		self.board= self.boards[z]
		self.board[x][y]= numberswap[z]
		for y in range(8):
			for x in range(8):
				if self.board[x][y] == '$': self.board[x][y]= '•'
		self.board[self.x][self.y]= '#'


	# Back Up Board State
	def backUp(self):
		self.boards.pop()
		self.board= self.boards[len(self.boards)-1]


	# Tests if Board is Complete
	def complete(self):
		complete= True
		for x in range(8):
			for y in range(8):
				if self.board[x][y] not in ('•', '$'):
					complete= False
					break

			if not complete: break
		return complete


	# Test from Current Position
	def test(self):
		while True:
			self.printBoard()
			if self.getMoves() == (): self.backUp()
			for move in self.getMoves():
				self.makeMove(move)
				break
			if self.complete():
				return self.board
				break
			if not self.first and len(self.boards) == 1: break

			#break # !!!


	# All Possible Moves
	def getMoves(self):
		moves= list()
		for move in self.moves():
			x, y= move
			if x < 0 or y < 0: continue
			if x > 7 or y > 7: continue
			if self.board[x][y] != '•': continue
			moves.append(move)
		return tuple(moves)



	# All Moves Relative to Knight
	def moves(self):
		x, y= self.x, self.y
		return (
			(x+1, y-2), (x+2, y-1),
			(x+2, y+1), (x+1, y+2),
			(x-1, y+2), (x-2, y+1),
			(x-2, y-1), (x-1, y-2) )


	# Print Board
	def printBoard(board):
		if type(board) is Knight: board= board.board
		for y in range(8):
			for x in range(8):
				print(board[x][y], end='')
			print()
		print()




# Test
def test():
	knight= Knight(3, 3)
	knight.printBoard()
	print(knight.moves() )
	print(knight.getMoves() )
	print()
	knight.makeMove(knight.getMoves()[0])
	knight.printBoard()
	print()
	knight.makeMove(knight.getMoves()[0])
	knight.makeMove(knight.getMoves()[0])
	knight.printBoard()
	print()
	knight.backUp()
	knight.printBoard()





# Run
if __name__ == "__main__":
	start()
	#test()

	exit()