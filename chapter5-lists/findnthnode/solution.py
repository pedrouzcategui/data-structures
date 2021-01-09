'''
 Write a function that returns the value of a given position in a Linked List

llist = 17 -> 30 -> 56 -> 6 -> 2

getValueOfPosition(2) // Returns 56
getValueOfPosition(0) // Returns 17
getValueOfPosition(5) // Return "The specified index does not exist in the Linked List"
'''

class LinkedList:
    def __init__(self):
        self.head = None

    def getValueOfIndex(self, index):
        current_index = 0
        node = self.head
        while(node != None):
            if(current_index == index):
                return node.data
            else: 
                current_index += 1
                node = node.next
        return "The specified index does not exist in this linked list"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


llist = LinkedList()
llist.head = Node(17)
second = Node(30)
third = Node(56)
fourth = Node(6)
fifth = Node(2)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

result = llist.getValueOfIndex(4)
print(result)