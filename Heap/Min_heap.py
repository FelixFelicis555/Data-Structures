class Min_Heap:
	def __init__(self):
		self.heaplist=[0]
		self.Currentsize=0

	

	def Insert(self,x):
		self.heaplist.append(x)
		self.Currentsize=self.Currentsize+1
		self.Lookup(self.Currentsize)

	def Lookup(self,i):#Take Care of positin of inserted element
		while i//2>0: #Parent should exist then only we v]can look up and we are looking up till root node
			if self.heaplist[i]<self.heaplist[i//2]:
				temp=self.heaplist[i]
				self.heaplist[i]=self.heaplist[i//2]
				self.heaplist[i//2]=temp
			i=i//2	

	def lookdown(self,i):
		while i*2 <= self.Currentsize:
			min_child=self.minChild(i)
			if self.heaplist[i]>self.heaplist[min_child]:
				temp=self.heaplist[i]
				self.heaplist[i]=self.heaplist[min_child]
				self.heaplist[min_child]=temp
			i=min_child

	def minChild(self,i):
		if i*2+1>self.Currentsize: #when only 2 nodes are there 1 parent and 1 child after deleting min
			return i*2
		else:
			if self.heaplist[i*2]<self.heaplist[i*2+1]:
				return i*2
			else:
				return i*2+1



	def extractMin(self):
		min=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.Currentsize]
		self.Currentsize=self.Currentsize-1
		self.heaplist.pop()
		self.lookdown(1)
		return min

	def buildHeap(self,alist):
		i=len(alist)//2
		self.Currentsize=len(alist)
		self.heaplist=[0]+alist[:]
		while (i>0):
			self.lookdown(i)
			i=i-1


def main():
	H=Min_Heap()
	H.buildHeap([9,5,6,2,3])
	H.Insert(50)
	print(H.heaplist)
	print(H.extractMin())
	print(H.extractMin())
	print(H.extractMin())



if __name__ == '__main__':
	main()

