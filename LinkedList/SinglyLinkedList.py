class Node:

	def __init__(self):
		self.next=None
		self.value=0


class LinkedList:

	def __init__(self):
		self.head=None

	def insertAtBeginning(self,x):
		temp=Node()
		temp.value=x
		if self.head==None:
			self.head=temp
			temp.next=None
		else:
			temp.next=self.head
			self.head=temp


	def insertAtEnd(self,x):
		temp=Node()
		temp.value=x
		if self.head==None:
			self.head=temp
			temp.next=None
		else:
			p=self.head
			while p.next!=None:
				p=p.next
			p.next=temp
				
	
	def insertAfter(self,x,p):
		temp=Node()
		temp.value=x
		if self.head==None:
			self.head=temp
			temp.next=None
		else:
			temp.next=p.next
			p.next=temp

	def insertAtIndex(self,i,x):
		temp=Node()
		temp.value=x
		if self.head==Node:
			self.head=temp
		else:
			p=self.head
			c=1
			while(c!=(i-1)):
				p=p.next
				c=c+1
			temp.next=p.next
			p.next=temp
			

	def printList(self):
		temp=self.head
		while temp!=None:
			print (temp.value)
			temp=temp.next

	def length(self):
		c=0
		p=self.head
		while(p!=None):
			p=p.next
			c=c+1
		print("Length:",end=" ")
		print(c)

	def isEmpty(self):
		if self.head==None:
			print("Empty")
		else:
			print("Non-Empty")

	def search(self,x):
		p=self.head
		#print(x)
		while(p!=None):
			#print(p.value)
			if(p.value==x):
				print("Found")
				break;
			else:
				p=p.next

	def delete(self,x):
		x.next=x.next.next

			



def main():
	L=LinkedList()
	L.isEmpty()
	L.insertAtBeginning(25)
	L.insertAtBeginning(30)
	L.insertAtBeginning(40)
	L.insertAtBeginning(45)
	L.insertAtEnd(20)
	L.insertAfter(5,L.head)
	L.insertAfter(10,L.head.next)
	L.printList()
	L.length()
	L.search(20)
	L.insertAtIndex(4,99)
	L.printList()
	L.length()
	L.isEmpty()
	L.search(30)
	L.delete(L.head)
	L.length()
	L.printList()
	n=input(("Enter the number u want to insert:"))
	L.insertAtBeginning(n)
	L.printList()


if __name__ == '__main__':
	main()
