# GCD and LCM

from math import *

num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
print()

print("GCD is : ",end="")
print(gcd(num1,num2))
print()

print("LCM is : ",end="")
print(int((num1*num2)/gcd(num1,num2)))

