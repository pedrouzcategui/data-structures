# Binary Search 

Given a sorten array arr[] of n elements, write a function to search a given element x in arr[];

The common approach would be to perform a _linear search_, nothing more to loop from the beggining of the array all the way
through the end, if not find, returns -1.

Time complexity for a linear search is O(n).

Another form to complete the same task is to perform a binary search.

```java
int arr[] = {2,5,8,12,16,23,38,56,72,91};
// Search the index of the element 23
```
The idea behind binary search is to use the information that the array is sorted and reduce the time complexity to O(log n)

The binary search is a function.

## How to implement a binary search?

1. Is mandatory that the array have to be sorted.
2. We need to find the mid element of the array