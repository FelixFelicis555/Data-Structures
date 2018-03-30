class Node:
    def __init__(self,val):
        self.next=None
        self.value=val
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,val):
        temp=Node(val)
        if self.head==None:
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
    def insertAtEnd(self,val):
        temp=Node(val)
        self.tail.next=temp

    def printLL(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next

def main():
    L=LinkedList()
    L.insert(10)
    L.insert(20)
    L.insert(30)
    L.insertAtEnd(0)
    L.printLL()
if __name__ == '__main__':
    main()