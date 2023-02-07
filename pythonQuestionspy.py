import math
# Write a program that prints "Hello, World!"
print("hello world")


# Write a program that takes two numbers as input and prints their sum
print("addition test")
# def add(x,y):
#     return x + y
# print("enter a number")
# x = input()
# print("enter another number")
# y = input()
# try:
#     x = int(x)
#     y = int(y)
# except(ValueError):
#     print("that isnt a number!")
# else:
#     print("the sum is")
#     print(add(x,y))
    
# Write a program that prints the first n Fibonacci numbers
print('fibonacci test')
def fibonacciNums(n):
    if(n == 0):
        return "youve asked me for nothing!"
    if(n == 1):
        return 0
    if(n == 2):
        return [0,1]    
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(n-2):
        fibo.append(fibo[i]+fibo[i+1])
    return fibo
print(fibonacciNums(30))
    
# Write a program that takes a string as input and
# prints the number of vowels in the string
print("vowels test")
def vowels(string):
    counter = 0
    for char in string:
        if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            counter += 1
    return counter
sent = "this sentance has x vowels"
print("this sentance has " + str(vowels(sent)) + " vowels")

# Write a program that takes a list of numbers as input 
# and prints the largest number in the list
print("largest number test")
def largest(nums):
    nums.sort()
    return nums[-1]
print(largest([0,22,1000,203,103,44,2]))

# Write a program that converts a temperature from Celsius to Fahrenheit
print("celcius to farenheight test")
def celToFar(temp):
    return temp*1.8 + 32
print(celToFar(0))

# Write a program that checks if a number is prime or not
print("prime test")
def isPrime(num):
    if(num <= 1):
        return False
    for i in range(2, int(num/2)+1):
        if(num % i ==0):
            return False
    return True
print(isPrime(11))
print(isPrime(3842))

# Write a program that calculates the factorial of a number
print("factorial test")
def factorial(num):
    return math.factorial(num)
print(factorial(11))
print(factorial(4))
print(factorial(1))
    
# Write a program that takes a string as input and returns the 
# number of occurrences of each letter in the string
print("letters in string test")
def lettersOccur(string):
    dic = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,
           "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
           "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    for char in string:
        for key, value in dic.items():
            if(char.lower() == key):
                dic[key] += 1
    return dic
string = "the quick brown fox jumps over the lazy dog"
print(string)
print(lettersOccur(string))

# Write a program that takes a list of strings and concatenates them 
#into a single string, separated by a space.
print("concatenate test")
def concatenate(strings):
    returnString = ""
    for string in strings:
        returnString += string + " "
    return returnString
print(concatenate(["hello", "world"]))

# Write a generator that yields the first n even numbers.

# Write a list comprehension that takes a list of numbers and returns 
# a new list containing only the positive numbers.

# Write a generator expression that computes the sum of the squares of 
# the first n positive numbers.

# Write a set comprehension that takes a list of strings and returns 
# a set of all the unique characters in the strings.

# Write a dictionary comprehension that takes a list of numbers and returns
# a dictionary where the keys are the numbers and the values are their squares.

# Write a generator that yields all the divisors of a number.

# Write a list comprehension that takes a list of strings and returns a
# new list containing only the strings that start with a specific letter.

# Write a generator expression that computes the dot product of two vectors
# represented as lists.

# Write a set comprehension that takes a list of strings and returns a set 
#of all the palindrome strings in the list.

# Write a dictionary comprehension that takes a list of numbers and returns 
# a dictionary where the keys are the numbers and the values are True if
# the number is even and False if the number is odd.