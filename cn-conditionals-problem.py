# Sum of even numbers till N - solution
'''
n = input()
def sumEvenNumbers(n):
    sumEven = 0
    for i in range(1, int(n) + 1):
        if i % 2 == 0:
            sumEven += i
    return sumEven

result = sumEvenNumbers(n)
print(result)

#  Fahrenheit to Celsius - solution
s = input()
e = input()
w = input()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def print_temperature_table(s, e, w):
    
    for fahrenheit in range(int(s), int(e) + 1, int(w)):
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(str(fahrenheit) + "\t" + str(int(celsius)))

print_temperature_table(s, e, w)

# Sum of even and odd
def sumEvenOdd(number):
    evenSum = 0
    oddSum = 0
    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            evenSum += digit
        else:
            oddSum += digit
    return evenSum, oddSum

N = int(input())
evenSum, oddSum = sumEvenOdd(N)
print(evenSum, oddSum)

# Find power of a number
x, n = map(int, input().split())

if x == 0 and n == 0:
    result = 1
else:
    result = str(x ** n)

print(result)

#  Factorial of a Number
def calculate_factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Error"
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    except ValueError:
        return "Error"

n = input()
result = calculate_factorial(n)
print(result)

#  N-th Fibonacci Number
from os import *
from sys import *
from collections import *
from math import *

def multiply_matrix(A, B, mod):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def power_matrix(A, n, mod):
    if n == 1:
        return A
    if n % 2 == 0:
        half_pow = power_matrix(A, n // 2, mod)
        return multiply_matrix(half_pow, half_pow, mod)
    else:
        half_pow = power_matrix(A, (n - 1) // 2, mod)
        return multiply_matrix(multiply_matrix(half_pow, half_pow, mod), A, mod)

def fibonacciNumber(n):
    if n <= 1:
        return n
    mod = 1000000007  # 1e9 + 7
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = power_matrix(base_matrix, n - 1, mod)
    return result_matrix[0][0]

# NOTE: To study above