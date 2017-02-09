import abc

class Observer:
	@abc.abstractmethod
	def onNewNote(self, note):
		pass

	@abc.abstractmethod
	def onNoteEdited(self, i, note):
		pass

	@abc.abstractmethod
	def onNoteDeleted(self, id):
		pass	