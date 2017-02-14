import time

class Note:
	def __init__(self, name, content, id=""):
		if id != "":
			self.__id = id
		else:
			self.__id = name #concatenado con la hora
		self.__name = name
		self.__content = content
		self.__lastModification = time.time() * 1000.0

	def getID(self):
		return self.__id

	def getName(self):
		return self.__name

	def getContent(self):
		return self.__content

	def __str__(self):
		return self.__name

	def __lt__(self, other):
		if isinstance(other, Note):
			return self.__lastModification < other.__lastModification
		else:
    		return NotImplemented

    def ___le__(self, other):
		if isinstance(other, Note):
	    	return self.__lastModification <= other.__lastModification
	    else:
	    	return NotImplemented

	def __eq__(self, other):
		if isinstance(other, Note):
			return self.__lastModification == other.__lastModification
		else:
			return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Note):
	    	return self.__lastModification != other.__lastModification
	    else:
			return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Note):
	    	return self.pages.__lastModification > other.__lastModification
	    else:
			return NotImplemented   

	def __ge__(self, other):
		if isinstance(other, Note):
	    	return self.pages.__lastModification >= other.__lastModification
	    else:
			return NotImplemented