class Max_Heap:
	def __init__(self):
		self.current_size=0
		self.heaplist=[0]
		self.sort=[0]


	def insert(self,x):
		self.heaplist.append(x)
		self.current_size=self.current_size+1
		self.lookup(self.current_size)

	def lookup(self,i):#updating the heap
		while i//2>0:
			if self.heaplist[i]>self.heaplist[i//2]:
				temp=self.heaplist[i]
				self.heaplist[i]=self.heaplist[i//2]
				self.heaplist[i//2]=temp
			i=i//2

	def heapify(self,i):
		while i*2<=self.current_size:
			if i*2+1>self.current_size:
				return i*2
			else:
				if self.heaplist[i*2]>self.heaplist[i*2+1]:
					max=i*2
				else:
					max=i*2+1
			if self.heaplist[max]>self.heaplist[i]:
				temp=self.heaplist[max]
				self.heaplist[max]=self.heaplist[i]
				self.heaplist[i]=temp
			i=max



	def Extract_Max(self):
		max=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.current_size]
		self.heaplist.pop()
		self.current_size=self.current_size-1
		self.heapify(1)
		return max

	def buildHeap(self,alist):
		i=len(alist)//2
		self.current_size=len(alist)
		self.heaplist[0]=alist[:]
		while i>0:
			self.heapify(i)
			i=i-1

	def HeapSort(self):
		self.sort=[]
		l=len(self.heaplist)
		for i in range(l):
			m=self.Extract_Max()
			self.sort.append(m)



def main():
	H=Max_Heap()
	H.insert(2)
	H.insert(5)
	H.insert(3)
	H.insert(7)
	H.insert(4)

	print(H.heaplist)
	print(H.Extract_Max())
	
	print(H.heaplist)
	H.HeapSort()
	print(H.sort)
if __name__ == '__main__':
	main()

