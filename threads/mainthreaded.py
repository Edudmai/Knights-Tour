###
# DO NOT USE
# TOO MANY THREADS
# ALMOST OCTUPLES IN LESS THAN A SECOND
###

# Imports
from copy import deepcopy
from threading import Thread, current_thread
from time import sleep


# Finals
MOVES= ( (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2) )
CHAR= {
	"empty": '_',
	"knight": '#'}
BASE66= (
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  #  0-9
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', # 10-19
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', # 20-29
	'u', 'v', 'w', 'x', 'y', 'z', '.', '!', '¡', '?', # 30-39
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', # 40-49
	'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', # 50-59
	'U', 'V', 'W', 'X', 'Y', 'Z')					  # 60-65
emptyBoard= lambda: [ [CHAR["empty"] for _ in range(8)] for _ in range(8)]


# Static
results= list()
threads= list()
thread_count= 0




# Start Function
def start():
	for y in range(4):
		for x in range(4):
			board= emptyBoard()
			board[x][y]= CHAR["knight"]
			boardThread(board, x, y, 0)

	while any(threads):
		print()
		print("Running...")
		print("Threads Alive:", len(threads) )
		print("Threads Total:", thread_count)
		print("Results Found:", len(results) )
		saveResults()
		sleep(15)
		alive= list()
		for thread in threads: alive.append(thread.is_alive() )
	print()
	print("Finishing...")
	print("Threads Total:", thread_count)
	print("Results Found:", len(results) )
	print()
	saveResults()

	printResults()




# Print Results
def printResults():
	for result in results: printBoard(result)




# Prints Board Legibly
def printBoard(board):
	for y in range(8):
		for x in range(8):
			print(board[x][y], end='')
		print()
	print()




# Save Results
def saveResults():
	with open("results.txt", 'w') as file:
		for board in results:
			for y in range(8):
				for x in range(8):
					file.write(board[x][y])
				file.write('\n')
			file.write('\n')




# Board Thread
def boardThread(board, x, y, iteration):
	global thread_count

	def threadFunc(board, x, y, iteration):

		new_boards= list()

		if CHAR["empty"] not in (board[x][y] for x in range(8) for y in range(8) ):
			results.append(board)
			threads.remove(current_thread() )
			return

		for move in MOVES:
			x2, y2= x+move[0], y+move[1]
			if x2 < 0 or y2 < 0: continue
			if x2 > 7 or y2 > 7: continue
			if board[x2][y2] != CHAR["empty"]: continue

			board_data= (deepcopy(board), x2, y2, iteration+1)
			board_data[0][x][y]= BASE66[iteration]
			board_data[0][x2][y2]= CHAR["knight"]
			new_boards.append(board_data)

		for board_data in new_boards:
			boardThread(*board_data)

		threads.remove(current_thread() )

	thread= Thread(target=threadFunc, args=(board, x, y, iteration) )
	threads.append(thread)
	thread_count+=1
	thread.start()




# Run
if __name__ == "__main__":
	start()

	exit()