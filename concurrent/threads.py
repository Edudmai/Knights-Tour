# Imports
from threading import Thread


# Statics
threads= list()




# Makes Function Run as Daemon
def daemonThread(thread_func):
	thread= Thread(target=thread_func)
	thread.daemon= True
	threads.append(thread)




# Starts Threads
def startThreads():
	for thread in threads:
		thread.start()