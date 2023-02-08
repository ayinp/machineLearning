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
    return " ".join(strings)
print(concatenate(["hello", "world"]))

# Write a generator that yields the first n even numbers.
print("even numbers test")
def evens(n):
    returnList = []
    evenCounter = 0
    i = 0
    while evenCounter < n:
        if(i%2 == 0):
            returnList.append(i)
            evenCounter += 1
        i += 1
    return returnList
print(evens(10))
        
# Write a list comprehension that takes a list of numbers and returns 
# a new list containing only the positive numbers.
print("only pos nums")
def posNums(lis):
    return [x for x in lis if x > 0]

nums = [1,2,-4,99,-100,43,2993,95,-255,-53,-31]
print(nums)
print(posNums(nums))

# Write a generator expression that computes the sum of the squares of 
# the first n positive numbers.
print("sum of squares test")
def sumOfSquares(n):
    return sum(num*num for num in range(n))
print(sumOfSquares(10))

# Write a set comprehension that takes a list of strings and returns 
# a set of all the unique characters in the strings.
print("unique characters test")
def uniqueChar(lis):
    return {c.lower() for s in lis for c in s}
strings = ["Hello", "World", "!"]
print(strings)
print(uniqueChar(strings))

# Write a dictionary comprehension that takes a list of numbers and returns
# a dictionary where the keys are the numbers and the values are their squares.
print("dictionary of squares test")
def dicOfSqrs(lis):
    return {n:n*n for n in lis}
nums = [1,5,3,2,7,4,3]
print(dicOfSqrs(nums))

# Write a generator that yields all the divisors of a number.
print("devisors test")
def devisors(n):
    return [i for i in (i for i in range(1, n+1) if n % i == 0)]
print(24)
print(devisors(24))
    
# Write a list comprehension that takes a list of strings and returns a
# new list containing only the strings that start with a specific letter.
print("beginning letter test")
def beginLetter(lis, letter):
    return [word for word in lis if letter.lower() == word[0].lower()]
sentances = ["Today I taught Tommy how to climb a tree", "tonight I will climb a tree", "everyone will climb a tree"]
print(sentances)
print(beginLetter(sentances, "t"))

# Write a generator expression that computes the dot product of two vectors
# represented as lists.
print("dot product test")
def dotProductList(v1, v2):
    return sum(a*b for a,b in zip(v1, v2))
v1 = [2,4,6]
v2 = [8,3,9]
print(v1, " dot ", v2)
print(dotProductList(v1, v2))

# Write a set comprehension that takes a list of strings and returns a set 
#of all the palindrome strings in the list.
print("palendrome test")
def palindromeStrings(lis):
    return [string for string in lis if string.lower() == string[::-1].lower()]
strings = ["racecar", "the", "Ayin", "Dad", "mOM"]
print(strings)
print(palindromeStrings(strings))

# Write a dictionary comprehension that takes a list of numbers and returns 
# a dictionary where the keys are the numbers and the values are True if
# the number is even and False if the number is odd.
print("odd even dictionary test")
def oddEvenDict(lis):
    return {n:True if n%2 == 0 else False for n in lis}
nums = [2,3,4,5,7,8,9,3,46,54,24,46,23]
print(oddEvenDict(nums))





