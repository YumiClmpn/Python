
# find area of a rectangle - solution sample 1
length, breadth = input("Length and Breadth: ").split()
area = int(length) * int(breadth)

print("Area:", str(area))

# find area of a rectangle - solution sample 2
length, breadth = input().split()
area = int(length) * int(breadth)

print(area)

# print name and age problem  - solution
name = input()
age = input()

print("The name of the person is", name, "and the age is", age + ".") # i need to use plus "+" sign to add period "." without space in printing

# swap two numbers problem - preset
from typing import List

def swapNumber(a:list,  b: list) -> None:
    # write your code here
    a, b = input().split()
    pass

#  swap two nummbers - solution  (approach 1)

    # Time complexity: O(1)
    # Space complexity: O(1)

def swapNumber(a, b):

    # Store the value of 'a' in 'temp'.
    temp = a[0]

    # Assign the value of 'b' to 'a' and the value of 'temp' to 'b'.
    a[0] = b[0]
    b[0] = temp

#  swap two nummbers - solution  (approach 2)


    # Time complexity: O(1)
    # Space complexity: O(1)

def swapNumber(a, b):

    # Store the value of 'a' in 'temp'.
    temp = a[0]

    # Assign the value of 'b' to 'a' and the value of 'temp' to 'b'.
    a[0] = b[0]
    b[0] = temp

# NOTE: STUDY ABOVE!!!

# calculate simple interest - solution

from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
p = int(input())
r = float(input())
t = int(input())

print(int((p * r * t) / 100))

# NOTE: Need to study the third problem