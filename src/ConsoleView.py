from Observer import Observer
from sys import stdin
from Note import Note
import os
import time

class ConsoleView(Observer):

	def __init__(self, controller):
		self.__notes = []
		self.__controller = controller
		self.__controller.addObserver(self)
		self.__controller.loadNotes()

	def display(self):
		exit = False

		while(not(exit)):
			self.printNotes()

			option = self.printOptionsAndReadOption()
			
			if (option == 1):#View note
				self.viewNote()
			elif (option == 2):#Add note
				self.readAndCreateNote()
			elif (option == 3):#Delete note
				self.readAndDeleteNote()
			elif (option == 4):#Edit note
				#TODO
				print("edit note")
				self.__controller.editNote
			elif (option == 0):#Exit
				exit = True

		print("Good bye")


	def viewNote(self):
		exit = False
		while (not(exit)):
			print("Enter the index of the note you want to see:")
			option = int(stdin.readline()[0])
			if (option > 0 and option <= len(self.__notes)):
				exit = True
			else:
				print("Please enter an index inside de correct range.")

		os.system('cls')
		print(self.__notes[option - 1].getName())
		print(self.__notes[option - 1].getContent())
		print("\n\n(Enter any character to return to main menu)")
		option = int(stdin.readline()[0])

	def readAndCreateNote(self):
		print("Enter a name: ")
		name = stdin.readline()[:-1]

		print("Enter a content: ")
		content = stdin.readline()[:-1]

		self.__controller.createNote(name, content)


	def readAndDeleteNote(self):
		exit = False
		while (not(exit)):
			print("Enter the index of the note you want to delete:")
			option = int(stdin.readline()[0])
			if (option > 0 and option <= len(self.__notes)):
				exit = True
			else:
				print("Please enter an index inside de correct range.")

		self.__controller.deleteNote(self.__notes[option - 1].getID(), option - 1)


	def printOptionsAndReadOption(self):
		exit = False
		while (not(exit)):
			print("Options:  1.View  2-Add  3-Delete  4-Edit  0-Exit")
			option = int(stdin.readline()[0])
			if (option == 0 or option == 1 or option == 2 or option == 3 or option == 4):
				exit = True
			else:
				print("Unknown option. Please select a correct value.")

		return option

	def printNotes(self):
		os.system('cls')
		i = 1
		for n in self.__notes:
			print(str(i) + " - " + n.getName())
			i += 1

	def onLoadNotes(self, notes):
		self.__notes = notes

	def onNewNote(self, note):
		self.__notes.insert(0, note)

	def onNoteEdited(self, note):
		del self.__notes[note.getID()]
		self.__notes[note.getID()] = note

	def onNoteDeleted(self, index):
		del self.__notes[index]
		print("Note deleted.")
		time.sleep(2)