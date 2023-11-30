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
'''
#  NOTE: please continue on the Find power of a number problem