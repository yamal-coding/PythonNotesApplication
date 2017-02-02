from Note import Note
from DataBase import DataBase

class Modelo:
	def __init__(self, database):
		self.__database = database

	def addObserver(self, observer):
		self.__observer = observer

	def loadNotes(self):
		notes = self.__database.loadNotes()
		#notificar a la vista que se han cargado las notas en la lista notes
		self.__observer.onLoadNotes(notes)

	def createNote(self, name, content):
		newNote = Note(name, content)
		self.__database.createNote(newNote)
		#notificar a la vista de que se ha aniadido una nueva nota con exito
		self.__observer.onNewNote(newNote)

	def deleteNote(self, id):
		self.__database.deleteNote(id)
		#notificar a la vista de que se ha eliminado la nota de identificador id

	def editNote(self, id, name, content):
		self.__database.editNote(id, name, content)
		#notificar cambios de la nota de identificador id a la vista