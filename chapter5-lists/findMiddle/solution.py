'''
  Write a function that finds the Middle value of a given linked list

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 3

EDGE CASE: In case that the linked list is even, we will print the second middle value.
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 4

EDGE CASE 2: If the value is None?

Algorithm:

1. Determine if the length of the linked list is even or odd
2.   If length is even
       Get the node in the position length/2 + 1
     Else
       Get the node in the position length/2 (remember that divisions in python round up automatically)
3.   Print the value
'''