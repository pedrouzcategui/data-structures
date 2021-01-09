# Write a function 'rotate' that rotates arr[] of size n by d elements
# Example:
#   arr = {1,2,3,4,5,6,7}
#   Input: rotate(arr,7,2)
#   Output: {3,4,5,6,7,1,2}

#  Solution 1: Slicing the array in two parts and append the cutted part to the other half.
#  
#  Algorithm:
#  1. Search for the element in the position 2 (using zero-based index) of the array
#  2. Cut or copy every element that is before that position
#  3. Append the cutted part to the other extreme of the array
#
#  Variables:
#  originalArr = represents the original array
#  firstHalf = represents the part that is extracted of the original array
#  secondHalf = represents the part keeped from the original array after the extraction
#  newArr = represents the append of the second and first half.
#
#
#

def rotate(array, size, skip):
    firstHalf = array[skip:]
    secondHalf = array[:skip]
    newArr = firstHalf+secondHalf
    return newArr

arr = [1,2,3,4,5,6,7]
print(rotate(arr,7,2))