'''
  Create a function that inserts a new node into a Linked List

  There are 3 possible ways to insert a node into a linked list
  1. In the head (at the front)
  2. In the middle given an specific index
  3. At the end

  This solution provides an code example of the first way
'''

class LinkedList:
  def __init__(self):
    self.head = None

  def appendAtFront(self, value):
    ## We need to make that this node points to the head
    nextNode = self.head   #2
    self.head = Node(value) # 1
    self.head.next = nextNode # setting reference
    while(nextNode.next): # Pointing to 3
      nextNode = nextNode.next # 3
      
      

  def printList(self):
    node = self.head
    print(node.data)
    while(node.next):
      node = node.next
      print(node.data)

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


llist = LinkedList()
llist.head = Node(2)
second = Node(3)
third = Node(4)
llist.head.next = second
second.next = third

llist.appendAtFront(1)
llist.printList()


