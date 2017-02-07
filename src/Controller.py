from Modelo import Modelo

class Controller:
	def __init__(self, modelo):
		self.__modelo = modelo

	def addObserver(self, observer):
		self.__modelo.addObserver(observer)

	def loadNotes(self):
		self.__modelo.loadNotes()

	def createNote(self, name, content):
		self.__modelo.createNote(name, content)

	def deleteNote(self, id, index):
		self.__modelo.deleteNote(id, index)

	def editNote(self, id, name, content):
		self.__modelo.editNote(id, name, content)