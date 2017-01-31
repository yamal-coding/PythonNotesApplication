from Observer import Observer

class ConsoleView(Observer):

	def __init__(self, controller):
		self.__notes = []
		self.__controller = controller
		self.__controller.addObserver(self)

	def printOptions():
		print("Options:  1-Add  2-Delete  3-Edit")

	def printNotes():
		for n in self.__notes

	def onNewNote():
		self.__notes.append

	def onNoteEdited():
		#TODO

	def onNoteDeleted():
		#TODO