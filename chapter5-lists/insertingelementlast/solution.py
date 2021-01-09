'''
  Create a function that inserts a node into the end of an linked list
'''

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        node = self.head
        print(node.data)
        while(node.next):
            node = node.next
            print(node.data)  

    def insertLast(self,value):
        node = self.head     # We need to traverse all the linked list, so we begin with the head
        while(node):
            node = node.next
            if(node.next == None):
                new_node = Node(value)
                node.next = new_node
                break



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
llist = LinkedList()
second = Node(2)
third = Node(3)
fourth = Node(4)


llist.head = Node(1)
llist.head.next = second
second.next = third
third.next = fourth

llist.printList()
print("\n")
llist.insertLast(5)
llist.printList()