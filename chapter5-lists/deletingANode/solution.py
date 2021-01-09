'''
  Write a function that deletes a node by its index
  LinkedList: 1 -> 2 -> A -> 3 -> 4
  LinkedList.delete(2) // Eliminates the A node
  
  Output: 1 -> 2 -> 3 -> 4

  Algorithm

  So lets focus on the delete part, lets delete the Node at index 2 of the example linked list
  
  0    1    2    3    4
  1 -> 2 -> A -> 3 -> 4

  Focus on:
  2 -> A -> 3

  1. We need to make 2 -> 3
  2. We need to make A -> None
  3. Print the length to verify
'''

class LinkedList:
    def __init__(self):
      self.head = None

    def pushValue(self, data):
        return data

    def deleteAtIndex(self, index):
        return index
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

