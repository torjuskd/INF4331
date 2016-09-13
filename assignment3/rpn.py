#!/usr/bin/env python3
# A simple calculator using a stack and reverse polish notation.
# ex: ./rpn.py "1 1 +"
# > 2
from math import sin
from math import cos
from math import sqrt
import sys

stack = []

def calc(userinput):
    if userinput == "p": #peek topmost item
        print(stack[-1])

    elif userinput == "v": #get square root
        num1=stack[-1]
        del stack[-1]
        result=eval("sqrt("+num1+")")
        print(result)
        stack.append(str(result))

    elif userinput == "sin": #find sin
        num1=stack[-1]
        del stack[-1]
        result=eval("sin("+num1+")")
        print(result)
        stack.append(str(result))

    elif userinput == "cos": #find cos
        num1=stack[-1]
        del stack[-1]
        result=eval("cos("+num1+")")
        print(result)
        stack.append(str(result))

    elif userinput in ("+", "-", "*", "/"):
        num2 = stack[-1]
        del stack[-1]
        num1 = stack[-1]
        del stack[-1]
        result = eval(num1+" "+userinput+" "+num2)
        stack.append(str(result))
        print(result)
        
    elif userinput == "stack": #Added easter-egg - print stack
        print(stack)

    else:
        num = userinput
        stack.append(num)

del sys.argv[0] #remove first arg (not really needed, could use arg[1] instead)
for arg in sys.argv[0].split(): #feed arguments into calc
    calc(arg)

while True: #keep taking inputs from keyboard
    userinputList = input('> ')
    for userinput in userinputList.strip().split():
        calc(userinput)
