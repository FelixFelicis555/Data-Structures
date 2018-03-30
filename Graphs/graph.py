#To represent a graph in a matrix and list

#Adjacent matrix
class Adjacent_Matrix:
	
	def __init__(self,n):
		self.matrix=[[0 for _ in range(n)] for _ in range(n)]#initializing the matrix with 0 

	def add_edges(self,v1,v2):
		self.matrix[v1][v2]=1
		self.matrix[v2][v1]=1

	def display(self):
		for row in self.matrix:
			print(row)

class Adjacent_list:
	
	def __init__(self,n):
		self.list=[[]for _ in range(n)]

	def add_edges(self,v1,v2):
		self.list[v1].append(v2)
		self.list[v2].append(v1)

	def display(self):

		for i,v in enumerate(self.list):
			print("Vertex {} :" .format(i),end='')
			print (v)


def main():
	n=int(input("Enter the number of vertices:"))
	#creating an object for both the classes
	L=Adjacent_list(n)
	M=Adjacent_Matrix(n)
	print ("Enter the edges(x to stop):")
	while True:
		e=input().split()
		if e[0]=='x':
			break
		else:
			v1,v2=map(int,e)
			L.add_edges(v1,v2)
			M.add_edges(v1,v2)

	print("Adjacent Matrix for the given graph:")
	M.display()
	print()
	print("Adjacent List for the given graph:")
	L.display()
	print()

if __name__ == '__main__':
	main()
