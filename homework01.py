# -*- coding: utf-8 -*-

def reverse(string):
    newString = ""
    strings = reversed(string.split())
    return " ".join(strings)
    
def replace(string, dic):
    newString = ""
    strings = string.split()
    newDic = {}
    for key, value in dic.items():
        newDic[key.upper()] = value
    return " ".join([newDic.get(s.upper(), s) for s in strings])


def toWord(thing):
    try:
        num = int(thing)
    except valueError:
        return thing
    else:
        return toStr1To100(num)
        
def toStr1To100(num):
    if(num < 10):
        return numbers[num][0]
    elif(num == 10):
        return "ten"
    elif(num == 11):
        return "eleven"
    elif(num == 12):
        return "twelve"
    elif(num == 13):
        return "thirteen"
    elif(num > 13 and num < 100):
        num = str(num)
        if(int(num)%10 == 0):
            return numbers[int(num[0])][2]
        if(int(num) > 13 and int(num) < 20):
            return numbers[int(num[1])][0] + numbers[int(num[0])][2]
        return numbers[int(num[0])][2] + " " + numbers[int(num[1])][0]
    elif(num == 100):
        return "one hundred!"
    return "UGH, I can't count that high, JEEZ!"
          
numbers = {
 1 : ["one",   "eleven", "teen"],
 2 : ["two",   "twelve", "twenty"],
 3 : ["three", "thir",   "thirty"],
 4 : ["four",  "four",   "forty"],
 5 : ["five",  "fif",    "fifty"],
 6 : ["six",   "six",    "sixty"],
 7 : ["seven", "seven",  "seventy"],
 8 : ["eight", "eight",  "eighty"],
 9 : ["nine",  "nine",   "ninty"],
 0 : ["zero",  "ten",    "hundred"]
}

print("REVERSE TEST")
print("hello world")
print(reverse("hello world"))
print("I am sooooo cool!")
print(reverse("I am sooooo cool!"))
print("\n \n")

print("REPLACE TEST")
string = "hello world"
dic = {"hello" : "goodbye", "world" : "cruel world"}
print(string)
print(replace(string, dic))
print("\n \n")

print("NUMBERS TEST")
for i in range(102):
    print(toWord(str(i)))

