
class Observer:
	@abstractmethod
	def onNewNote(self, note):
		pass

	@abstractmethod
	def onNoteEdited(self, note):
		pass

	@abstractmethod
	def onNoteDeleted(self, id):
		pass	