class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        node = self.head
        print(node.data) # This is the actual value of the node
        while(node.next):    
          node = node.next
          print(node.data) ## This is the value of the second node

'''
  Create a function that prints all the elements of a linked list
  1. The actual linked list have all the connected nodes,
  2. We need to traverse all of the nodes, beggining with the head,
  3. The head is a Node Object,
  4. After all the elements of the linked list is linked, we can print all of the elements,
  5. We need to track the actual node and print the value, we set the node to self.head because is the first node.
  6. After that, we need to switch to the other node, so if node.next isn't null, that means that another node still exist in the linked list
  7. Then, we update the node by calling node.next and setting it to the node variable.
  8. The cycle will stop when node.next is a falsy value, and that is (in python) None.
'''

llist = LinkedList()
llist.head = Node(1) ## Remember, the head is a Node, and you have access to the next variable
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printList()