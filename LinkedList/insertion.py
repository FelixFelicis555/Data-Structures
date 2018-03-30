from formation import LinkedList
class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next

    def insertAtBeg(self,val): #insert a node at beginning takes O(1) time complexity
        temp=Node(val)
        if self.head == None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

    def insertAtEnd(self,val): #inserting a node at the end takes O(n) where n is the length of length of linked list
        if self.head == None:
            self.head=Node(val)
        else:
            tmp=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=Node(val)

    def insertAfternode(self,p,val): #this also takes O(1) time
        temp=Node(val)
        temp.next=p.next
        p.next=temp

    def insertAtIndex(self,i,val):
        temp=self.head
        new_node=Node(val)
        c=1
        while c!=i-1:
            temp=temp.next
            c=c+1
        new_node.next=temp.next
        temp.next=new_node




def main():
    L=LinkedList()
    L.insertAtBeg(5)
    L.insertAtBeg(45)
    L.insertAtBeg(100)
    L.insertAtEnd(23)
    L.insertAtIndex(3,85)
    L.insertAtEnd(5)
    L.insertAfternode(L.head.next,99)
    L.printLL()

if __name__ == '__main__':
    main()


