class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def printListList(self):
        currentNode = self.head
        while currentNode:
            print(f"{currentNode.data}")
            currentNode = currentNode.next

    def reverseList(self):
        head = self.head
        current = head
        previous = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current=next
        self.head = previous


ll = SLinkedList()
ll.insertAtBeginning('F')
ll.insertAtBeginning('E')
ll.insertAtBeginning('D')
ll.insertAtBeginning('C')
ll.insertAtBeginning('B')
ll.insertAtBeginning('A')
ll.printListList()
print("###########")
ll.reverseList()
ll.printListList()