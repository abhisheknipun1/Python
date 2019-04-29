# Matrix

#pip3 install numpy

from numpy import *

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)

# array using numpy module

a = array([1, 2, 3])
print(a)               # Output: [1, 2, 3]
print(type(a))

# Matrix using numpy module

A = array([[2, 4], [5, -6]])
B = array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print(C)

D = A * B # Matrix Multiplication

print(D)

# Transpose of Matrix

print(A.transpose())
