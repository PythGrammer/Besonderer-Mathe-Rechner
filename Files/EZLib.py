import sys
import time
import random

def println(object,type):
    if(type == "s"):
        print(object,end="")
    elif(type == "i"):
        print(str(object),end="")
    elif(type == "l"):
        for thing in object:
            str(thing)
            print(thing,end="")
    elif(type == "b"):
        print(str(object),end="")
    else:
        print("Syntax error!")

def wait(x):
    time.sleep(x)

def coinflip():
    x = random.randint(0,1)
    if(x == 0):
        println(["Coin: ", "Head"], "l")
    elif(x == 1):
        println(["Coin: ", "Tails"], "l")
    return x

def exit(running):
    running = False
    print("System: EXIT")
    sys.exit()

def calc(mode,num1,num2):
    if(mode == "add"):
        return num1 + num2
    elif(mode == "sub"):
        return num1 - num2
    elif(mode == "mul"):
        return num1 * num2
    elif(mode == "div"):
        return num1 / num2

def til(thing,list):
    if(thing in list):
        return True
    else:
        return False

def buildList(o1,o2,o3,o4,o5):
    x = [o1,o2,o3,o4,o5]
    return x

def plus(x):
    x = x + 1
    return x

def minus(x):
    x = x - 1
    return x

def printList(list):
    i = 0
    while i < len(list):
        print(list[i], end=" ")
        i = i + 1