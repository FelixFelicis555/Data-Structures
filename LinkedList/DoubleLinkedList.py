class Node:
	def __init__(self):
		self.prev=None
		self.next=None
		self.value=0

class LinkedList:
	def __init__(self):
		self.head=None

	def insertAtBeginning(self,x):
		temp=Node()
		temp.value=x
		if(self.head==None):
			self.head=temp
			temp.prev=self.head
		else:
			temp.next=self.head
			self.head=temp
			self.prev=self.head


	def printList(self):
		c=0
		p=self.head
		while(p!=None):
			print(p.value);
			p=p.next
		

def main():
	L=LinkedList()
	L.insertAtBeginning(19)
	L.insertAtBeginning(29)
	L.printList()

if __name__ == '__main__':
	main()
