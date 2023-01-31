# -*- coding: utf-8 -*-

def reverse(string): 
    strings = reversed(string.split())
    return " ".join(strings)
    
def replace(string, dic):
    strings = string.split()
    newDic = {}
    for key, value in dic.items():
        newDic[key.upper()] = value
    return " ".join([newDic.get(s.upper(), s) for s in strings])


def toWord(thing):
    try:
        num = int(thing)
    except ValueError:
        return thing
    else:
        return toStr1To100(num)
        
def toStr1To100(num):
    #single digets
    if(num < 10):
        return numbers[num][0]
    #weird teens
    elif(num == 10):
        return "ten"
    elif(num == 11):
        return "eleven"
    elif(num == 12):
        return "twelve"
    elif(num == 13):
        return "thirteen"
    elif(num == 15):
        return "fifteen"
    #less wierd numbers
    elif((num > 13 and num < 100) and num != 15):
        num = str(num)
        #more teens
        if(int(num) > 13 and int(num) < 20):
            return numbers[int(num[1])][0] + numbers[int(num[0])][1]
        #nums ending in zero
        if(int(num)%10 == 0):
            return numbers[int(num[0])][1]
        #all the other "normal" numbers
        return numbers[int(num[0])][1] + " " + numbers[int(num[1])][0]
    #one hundred lmao
    elif(num == 100):
        return "one hundred!"
    return "UGH, I can't count that high, JEEZ!"
          
numbers = {
 1 : ["one",    "teen"],
 2 : ["two",    "twenty"],
 3 : ["three",   "thirty"],
 4 : ["four",    "forty"],
 5 : ["five",    "fifty"],
 6 : ["six",     "sixty"],
 7 : ["seven",   "seventy"],
 8 : ["eight",   "eighty"],
 9 : ["nine",    "ninty"],
 0 : ["zero",    "hundred"]
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

