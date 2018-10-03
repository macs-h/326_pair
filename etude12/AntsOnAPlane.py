#!/usr/bin/env python3
import sys
from Ant import Ant
while True:
    dnaDict = {}
    inp = "start"
    maxSteps= -1
    firstLine = True
    defaultSym = ' '
    totalInput = []
    while True:
        
        try:
            inp = input()
            if inp == "":
                exit()
            parsedIn = inp.split(' ')
            if(len(parsedIn) == 1):
                #the final int showing steps
                maxSteps = int(parsedIn[0])
                if maxSteps == -1:
                    print("Input the positive amount of steps to traverse")
                    continue
                else:
                    totalInput.append(inp)
                    break
                    
            elif inp[0] != '#':
                # # comments will be skipped over
                # parsedIn = inp #seperates input into 3 parts, symbol, direction to go, what symbol to change
                dnaDict[parsedIn[0]] = (parsedIn[1].upper(), parsedIn[2])  #WAdd(parsedIn[0],(parsedIn[1], parsedIn[2]))
                if firstLine:
                    defaultSym = parsedIn[0]
                    firstLine = False
                totalInput.append(inp)
        except EOFError:
            exit()
    ant = Ant(dnaDict, defaultSym)
    currentStep = 0
    currentPos = (0,0)
    while currentStep < maxSteps:
        currentPos = ant.move(currentPos)
        currentStep+=1
    for inp in totalInput:
        print(inp)
    print("# {0} {1}\n".format(currentPos[0], currentPos[1]))
    try:
        input()
    except EOFError:
        exit()





