# Node of doubly linked list:
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DLL:
    def __init__(self):
        self.head = None

    def insertAtFront(self, newData):
        newNode = Node(data=newData)
        newNode.next = self.head
        newNode.prev = None
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def printList(self, node):
        while(node is not None): 
            print (" % d" %(node.data)) 
            last = node 
            node = node.next
  
        print ("\nTraversal in reverse direction")
        while(last is not None): 
            print (" % d" %(last.data),)
            last = last.prev

dllist = DLL()
dllist.insertAtFront(6)  # 6 -> None
dllist.insertAtFront(7)    # 7 -> 6 -> None
dllist.insertAtFront(1)    # 1 -> 7 -> 6 -> None
dllist.insertAtFront(4)  # 1 -> 7 -> 6 -> 4 -> None
dllist.insertAtFront(2)

dllist.printList(dllist.head)