from numpy import *
"""
from array import *

arr = array("i", [1, 2, 3, 4])
print(arr)

arr2 = array(arr.typecode, [5, 6, 7, 8])
print(arr2)
"""


"""
arr1 = array([1, 2, 3, 4])

print("Arr1: ", arr1)

arr2 = array([5, 8, 9, 7])
arr2 = arr2 + 2

print("Arr2: ", arr2)

arr3 = arr1 + arr2

print(arr3)

#Shadow copy

arr5 = array([1,2,5,6])
arr6 = arr5.view()
arr5[0] = 8

print("arr5: ", arr5)
print("arr6: ", arr6)

print("arr5.id: ", id(arr5))
print("arr6.id: ", id(arr6))

#Deep copy

arr7 = array([1,2,5,6])
arr8 = arr7.copy()
arr7[0] = 8

print("arr7: ", arr7)
print("arr8: ", arr8)

print("arr7.id: ", id(arr7))
print("arr8.id: ", id(arr8))
"""

#Multy dimentional array
arr1 = array(
    [
        [1,2,3,4],
        [5,6,7,8]
    ]
)

print(arr1) #the array
print(arr1.ndim) #number of dimentions
print(arr1.shape) #number of rows and coloms
print(arr1.size) #number of elements

arr2 = arr1.flatten()
print(arr2) #convert two dimentional array into one dimentional

arr3 = arr2.reshape(2,4)
print(arr3) #convert one dimentional array into two dimentional

arr4 = arr2.reshape(2,2,2)
print(arr4) #convert one dimentional array into three dimentional (two, two dimentional)

m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(m) #matrix
print(diagonal(m))