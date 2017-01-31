
class Observer:
	@abstractmethod
	def onNewNote(self, note):
		pass

	@abstractmethod
	def onNoteEdited():
		pass

	@abstractmethod
	def onNoteDeleted():
		pass	