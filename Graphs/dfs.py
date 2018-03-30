
class Stack:

	def __init__(self):
		self.stack=[]

	def Push(self,v):
		self.stack.append(v)

	def Pop(self):
		return self.stack.pop()

	def is_Empty(self):
		return len(self.stack)==0		

class Graph:
	def __init__(self,n):
		self.list=[[] for _ in range(n)]

	def add_edges(self,v1,v2):
		self.list[v1].append(v2)
		self.list[v2].append(v1)

	def dfs(self,source):
		visited=[]
		S=Stack()
		S.Push(source)
		visited.append(source)
		print(source,end=' ')
		while not S.is_Empty():
			node=S.Pop()
			for neighbour in self.list[node]:
				if neighbour not in visited:
					visited.append(neighbour)
					print(neighbour,end=' ')
					S.Push(neighbour)
					node=neighbour
					




def main():

	n= int(input("Enter tne number of vertices:"))
	G=Graph(n)
	print("Enter the edges(x to stop):")
	while True:
		e=input().split()
		if e[0]=='x':
			break
		else:
			v1,v2=map(int,e)
			G.add_edges(v1,v2)

	print("Enter the source vertex:")
	source=int(input())
	G.dfs(source)

if __name__ == '__main__':
	main()