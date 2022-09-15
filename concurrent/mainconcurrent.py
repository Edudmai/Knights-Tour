# Imports
import os
from copy import deepcopy
from threads import daemonThread, startThreads
from datetime import datetime
from time import sleep, time


# Finals
DELAY= 10
START_TIME= time()
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
todos= list()
todo_count= 0




# Start Function
def start():

	log("Starting at:		", datetime.now() )
	log()



	todo_todos= list()
	for y in range(4):
		for x in range(4):
			pass
	board= emptyBoard()
	board[0][0]= CHAR["knight"]
	todo_todos.append( (board, 0, 0, 0) )

	startThreads()

	i= 0
	for todo in todo_todos:
		log("Starting…")
		log(f"Position:			 ({todo[1]}, {todo[2]})")
		todos.append(todo)

		while any(todos):
			avg= 0
			for todo in todos:
				avg+=todo[3]
			avg/=len(todos)
			total_progress= ( (i/16)+( (avg/60)/16) )*100
			current_progress= (avg/60)*100
			log()
			log("Running…")
			log("Time Elapsed:		", getTime() )
			log("Total Progress:		", progress(total_progress) )
			log("Current Progress:	", progress(current_progress) )
			log("Results Found:		", len(results) )
			log("Active TODOs:		", len(todos) )
			log("TODOs Completed:	", todo_count)
			log("Average iteration:	", avg)
			
			save()
			sleep(DELAY)

		log()
		i+=1

	log("Finishing…")
	log("Time Elapsed:		", getTime() )
	log("Results Found:		", len(results) )
	log("TODOs Completed:	", todo_count)
	save()
	log()

	printResults()




# Board Thread
@daemonThread
def doTodos():
	global todo_count

	while True:
		for todo in todos:
			board, x, y, iteration= todo

			todo_count+= 1

			if CHAR["empty"] not in (board[x][y] for x in range(8) for y in range(8) ):
				results.append(board)
				todos.remove(todo)
				

			for move in MOVES:
				x2, y2= x+move[0], y+move[1]
				if x2 < 0 or y2 < 0: continue
				if x2 > 7 or y2 > 7: continue
				if board[x2][y2] != CHAR["empty"]: continue

				board= deepcopy(board)
				board[x][y]= BASE66[iteration]
				board[x2][y2]= CHAR["knight"]
				todos.append( (board, x2, y2, iteration+1) )

			todos.remove(todo)









# Logs to file and prints
def log(*data, end='\n'):
	print(*data, end=end)
	with open("log.txt", 'a') as log:
		for dat in data:
			log.write(str(dat)+' ')
		log.write('\n')




# Progress Bar
def progress(percent):
	return "["+"#"*int(percent/5)+"_"*(20-int(percent/5) )+"] "+str(percent)+"%"




# Get Time
def getTime():
	elapsed_time= time()-START_TIME
	hours= int(elapsed_time//(60*60) )
	minutes= int( (elapsed_time//60)-(hours*60) )
	seconds= elapsed_time-(minutes*60)
	return f"{hours} hrs, {minutes} mins, {seconds} secs"




# Print Results
def printResults():
	for result in results: printBoard(result)




# Prints Board Legibly
def printBoard(board):
	for y in range(8):
		for x in range(8):
			log(board[x][y], end='')
		log()
	log()




# Save Results
def save():
	log("Saving…")
	with open("results.txt", 'w') as file:
		for board in results:
			for y in range(8):
				for x in range(8):
					file.write(board[x][y])
				file.write('\n')
			file.write('\n')









# Run
if __name__ == "__main__":
	start()

	exit()