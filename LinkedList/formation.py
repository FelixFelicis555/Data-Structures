class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        temp=self.head
        while temp!=None:
            print(temp.value,end=" ")
            temp=temp.next
def main():
    L=LinkedList()
    L.head=Node(1)
    second=Node(2)
    third=Node(3)
    L.head.next=second
    second.next=third
    L.printLL()


if __name__ == '__main__':
    main()

