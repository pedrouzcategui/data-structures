'''
Write a function that returns true or false depending if an specified item is on the LinkedList

Linked List =   1 -> 2 -> 3
searchItem(2) // Return True
searchItem(4) // Return False

Algorithm 

while(node.next):
    if (node.data == value)
      return true
    else 
     node = node.next
return false


'''

class LinkedList:
    def __init__(self):
        self.head = None

    def searchItem(self, value):
        node = self.head
        while(node.next):
            if (node.data == value):
              return True
            else: 
             node = node.next
        return False
    
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
second = Node(2)
third = Node(3)
llist.head = Node(1)
llist.head.next = second
second.next = third

llist.printList()
isOnList = llist.searchItem(4)
print(isOnList)