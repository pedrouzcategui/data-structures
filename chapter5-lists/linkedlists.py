class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

llist = LinkedList() # Inicializando el objeto linked lis

llist.head = Node(1) # Asignando la cabeza
second = Node(2)
third = Node(3)

'''
Hasta ahora, esto va asi:

llist.head     second      third
    |            |           |
    |            |           |
[1,None]      [2,None]    [3,None]

'''

llist.head.next = second # Linking the first node to the second

'''
Hasta ahora, esto va asi:

llist.head     second      third
    |            |           |
    |            |           |
[1,o]-------->[2,None]    [3,None]
'''

second.next = third # Enlazando la referencia del segundo al tercero

'''
Hasta ahora, esto va asi:

llist.head     second      third
    |            |           |
    |            |           |
[1,o]-------->[2,o]------>[3,None]
'''
