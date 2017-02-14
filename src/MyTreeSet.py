class MyTreeSet:
	'''sorted tree. Each node has an element and two possible childs. If
	there is not one of the both child, it is declared as None'''

	def __init__(self, elem, left=None, right=None):
		self.__leftChild = left
		self.__elem = elem
		self.__rightChild = right


	def getElem(self):
		return self.__elem

	def contains(self, e):
		if (self.__elem == e):
			return True

		if (self.__elem < e and self.__leftChild != None):
			return self.__leftChild.contains(e)
		else:
			return False

		if (self.__rightChild != None):
			return self.__rightChild.contains(e)
		else:
			return False

	def insert(self, e):
		if (e < self.__elem):
			if (self.__leftChild == None):
				self.__leftChild = MyTreeSet(e)
				return True
			return self.__leftChild.insert(e)
		elif (e > self.__elem):
			if (self.__rightChild == None):
				self.__rightChild = MyTreeSet(e)
				return True
			return self.__rightChild.insert(e)
		else
			return False #the element already exists
		
	def preorden(self):
		if (self.__leftChild != None):
			self.__leftChild.preorden()

		print(self.__elem)

		if (self.__rightChild != None):
			self.__rightChild.preorden()

	def inorden(self):
		print(self.__elem)

		if (self.__leftChild != None):
			self.__leftChild.inorden()

		if (self.__rightChild != None):
			self.__rightChild.inorden()