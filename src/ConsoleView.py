from Observer import Observer
from sys import stdin
from Note import Note

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
				#TODO
				print("view note")
			elif (option == 2):#Add note
				print("Enter a name: ")
				name = stdin.readline()[:-1]

				print("Enter a content: ")
				content = stdin.readline()[:-1]

				self.__controller.createNote(name, content)
			elif (option == 3):#Delete note
				#TODO
				print("delete note")
				self.__controller.deleteNote
			elif (option == 4):#Edit note
				#TODO
				print("edit note")
				self.__controller.editNote
			elif (option == 0):#Exit
				exit = True

		print("Good bye")


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
		#for k in self.__notes.keys():
		#	print(self.__notes[k].getName())
		i = 1
		for n in self.__notes:
			print(str(i) + " - " + n)
			i += 1

	def onLoadNotes(self, notes):
		self.__notes = notes

	def onNewNote(self, note):
		self.__notes[note.getID()] = note
		print("Note added!")

	def onNoteEdited(self, note):
		del self.__notes[note.getID()]
		self.__notes[note.getID()] = note

	def onNoteDeleted(self, id):
		del self.__notes[id]