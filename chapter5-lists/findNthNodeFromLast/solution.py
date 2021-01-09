'''
Write a function that prints the value of a node beggining to count from the last node

Example:
Linked List: A -> B -> C -> D
Input: 3
Output: B

Algorithm

1. Find the length of the Linked List
    4    3    2    1
    A -> B -> C -> D

    getLength() // Returns 4

2. Then, traverse it again to the (Length - Value) Index and return that value
    getValueOfIndex(4 - 3)

'''

class LinkedList:
    def __init__(self):
        self.head = None
    
    def getLength(self):
        length = 0
        node = self.head
        while(node != None):
            length += 1
            node = node.next
        return length

    def getValueOfIndex(self, value):
        index = 0
        node = self.head
        while(node is not None):
            if(value == index):
                return node.data
            else:
                node = node.next
                index += 1
    
    def getReverseValue(self, value = 0):
        length = self.getLength()

        if(value > length or value <= 0 or value == None):
            return "The specified index couldn't be found or is not specified"

        return self.getValueOfIndex(length - value)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

llist = LinkedList()

llist.head = Node("A")
second = Node("B")
third = Node("C")
fourth = Node("D")

llist.head.next = second
second.next = third
third.next = fourth

value = llist.getReverseValue()