'''

Write a program that reverses a linked list

Option 1

Input:   1 -> 2 -> 3
Output:  3 -> 2 -> 1

Simple Case:
Input: 1 -> 2 -> 3 -> None
Output: 3 -> 2 -> 1 -> None
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

    def reverseList(self):
        

        





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

# llist.printList()
llist.reverseList()
llist.printList()
