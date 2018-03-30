class Graph:
	def __init__(self,n):
		self.list=[[] for _ in range(n)]

	def add_Edges(self,v1,v2):
		self.list[v1].append(v2)
		self.list[v2].append(v1)

	def dfs(self,source):
		sour


def main():
	n=int(input("Enter number of edges"))
	G=Graph(n)
	print("Enter the edges(x to stop):")
	while True:
		e=input().split()
		if e[0]=='x':
			break
		else:
			v1,v2=map(int,e)
			G.add_Edges(v1,v2)

	source=int(input("Enter the source:"))
	print("After doing dfs:")
	G.dfs(source)

