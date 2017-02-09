from Note import Note
from DataBase import DataBase

class Modelo:
	def __init__(self, database):
		self.__database = database

	def addObserver(self, observer):
		self.__observer = observer

	def loadNotes(self):
		notes = self.__database.loadNotes()

		self.__observer.onLoadNotes(notes)

	def createNote(self, name, content):
		newNote = Note(name, content)
		self.__database.createNote(newNote)

		self.__observer.onNewNote(newNote)

	def deleteNote(self, id, index):
		self.__database.deleteNote(id)

		self.__observer.onNoteDeleted(index)

	def editNote(self, i, id, name, content):
		self.__database.editNote(id, name, content)
		
		self.__observer.onNoteEdited(i, Note(name, content, id))