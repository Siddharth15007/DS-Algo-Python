# get concept and code from tutorialspoint for practice


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLL:
    def __ini__(self):
        self.head = None

    def TraverseList(self):
        traverse = self.head
        while traverse is not None:
            print(traverse.data)
            traverse = traverse.next

    # Insert the new data (At the begining of the list):
    def InsertAtBegining(self, newData):
        NewNode = Node(newData)

    # Update the new nodes next value to existing node
        NewNode.next = self.head
        self.head = NewNode


    # insert the new node (At the End of the list):
    def InsertAtEnd(self, newData):
        NewNode = Node(newData)
        if self.head == None:
            self.head = NewNode
            return
        lastData = self.head
        while lastData.next:
            lastData = lastData.next
        lastData.next = NewNode
    
    # insert new node at between two nodes of the list:
    def InsertInBetween(self,midNode,newData):
        if midNode is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newData)
        NewNode.next = midNode.next
        midNode.next = NewNode

    # delete node:
    def DeleteNode(self,key):
        HeadData = self.head
        #print("HeadData",HeadData.data)
        if HeadData == key:
            self.head = HeadData.next
            HeadData = None
            return
        while HeadData is not None:
            if HeadData.data == key:
                break
            prev = HeadData
            #print("prev",prev.data)
            HeadData = HeadData.next
        if HeadData == None:
            return
        prev.next = HeadData.next
        HeadData = None    

list1 = SLL()
list1.head = Node("X")
e2 = Node("Y")
e3 = Node("Z")

list1.head.next = e2
e2.next = e3

# insert new node at the begining
list1.InsertAtBegining("A")

#insert new node at the end
list1.InsertAtEnd("B")

#insert new node in between
list1.InsertInBetween(list1.head.next,"XY")

list1.DeleteNode("XY")

list1.TraverseList()