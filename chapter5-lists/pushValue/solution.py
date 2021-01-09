'''
  Create an algorithm that push a value into the end of a LinkedList
  
  ll =  1 -> 2 -> 3
  ll.push(4)
  ll = 1 -> 2 -> 3 -> 4

  Algorithm:
  
  1. We need to find the end of the LinkedList
    
    node = self.head

  2. When we had found the end node, we will create a new node


  3. Then, we will point the end node to the new node
  
  
  4. After that, we will break from the cycle
'''

class LinkedList:
    def __init__(self):
        self.head = None

    def pushValue(self, value):
       return value

    def printList(self):
        node = self.head
        print(node.data)
        while(node.next):
            node = node.next
            print(node.data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

llist = LinkedList()
llist.pushValue(1)
llist.pushValue(2)
llist.printList()


