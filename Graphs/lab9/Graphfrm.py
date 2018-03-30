class Adjacency_Matrix:
	def __init__(self,n):
		self.adMatrix=[[0 for _ in range(n)] for _ in range(n)] #n*n matrix created

	def add_edge(self,a1,a2):#where a1 and a2 are vertex 1 and vertex 2
		self.adMatrix[a1][a2]=1
		self.adMatrix[a2][a1]=1

	def display(self):
		for i in self.matrix:
			print(i) #i here will print row wise


class Adjacency_List:

	def __init__(self,n):
		self.list=[[]for _ in range(n)]

	def add_edge(self,a1,a2):
		self.list[a1].append(a2)
		self.list[a2].append(a1)

	def display(self):
		for i
