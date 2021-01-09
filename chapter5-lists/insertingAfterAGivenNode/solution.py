'''
  Create a function that insert a new_node after another node into a given linked list

  Steps
  1 -> 2 -> 3 -> 5
  Suppose that we want to insert after the 2 node.
  
  1. Check the data of the node 
      if the node is equal to the data argument, we need to insert that node
      1.2 Pointing that node to the new Node
      1.3 then, that new node, will point to the previous node.next node

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

    def insertAfter(self, data, value):
        node = self.head 
        while(node):
            if(node.data == data):
                previous_node = node 
                new_node = Node(value) 
                new_node.next = previous_node.next 
                previous_node.next = new_node 
                break
            else:
                node = node.next
        print("No node was finded")
        


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

llist = LinkedList()
second = Node(2)
third = Node(3)
five = Node(5)

llist.head = Node(1)
llist.head.next = second
second.next = third
third.next = five

llist.printList()
llist.insertAfter(3,4)
llist.printList()

    