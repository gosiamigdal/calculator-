import math

def add(*args):
    result = 0
    for index,num in enumerate(args):
        print num[index]
        num[index] = int(num[index])
        result += num[index]
    return result

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return square(num1) * num1

def power(num1, num2):
    return num1 ** num2 

def mod(num1, num2):
    return num1 % num2