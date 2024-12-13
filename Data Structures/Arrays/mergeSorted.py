# Merge two given sorted arrays into one resulting sorted array
# Given arrays are: 
array1 = [1, 3, 20, 50]
array2 = [4, 5, 9, 40]

def mergeSortedArrays(arr1, arr2):
    # ads both the arrays into one single merged array
    sortedArr = array1 + array2
    
    # Use the built in sort() method in python to sort the new merged array
    sortedArr.sort()
    
    # print the result 
    print(sortedArr)

mergeSortedArrays([0,3,4,31], [3,4,6,30])
