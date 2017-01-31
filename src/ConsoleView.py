from Observer import Observer
from sys import stdin

class ConsoleView(Observer):

	def __init__(self, controller):
		self.__notes = {}
		self.__controller = controller
		self.__controller.addObserver(self)

	def display(self):
		exit = False

		while(not(exit)):
			printNotes

			option = printOptionsAndReadOption
			
			if (option == 1):#View note
				#TODO
			elif (option == 2):#Add note
				#TODO
			elif (option == 3):#Delete note
				#TODO
			elif (option == 4):#Edit note
				#TODO
			elif (option == 0):#Exit
				exit = True

		print("Good bye")


	def printOptionsAndReadOption(self):
		exit = False
		while (not(exit)):
			print("Options:  1.View  2-Add  3-Delete  4-Edit  0-Exit")
			option = int(stdin.read(1))
			if (option == 0 || option == 1 || option == 2 || option == 3 || option == 4):
				exit = True
			else:
				print("Unknown option. Please select a correct value.")

		return option

	def printNotes():
		for k in self.__notes.keys():
			print(self.__notes[k].getName())

	def onNewNote(self, note):
		self.__notes.[note.getID()] = note

	def onNoteEdited(self, note):
		del self.__notes[note.getID()]
		self.__notes[note.getID()] = note

	def onNoteDeleted(self, id):
		del self.__notes[id]