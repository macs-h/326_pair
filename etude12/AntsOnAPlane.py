from Ant import Ant
# Dictionary<char, (string dir, string nState)> dnaDict = new Dictionary<char, (string, string)>();
dnaDict = {}
inp = "start"
maxSteps= 0
firstLine = True
defaultSym = ' '
totalInput = []
while inp != "":
    inp = input()
    totalInput.append(inp)
    if(len(inp) == 1):
        #the final int showing steps
        maxSteps = int(inp)
        inp = "" #so will end input (count is the last thing they give)
    elif inp[0] != '#':
        # # comments will be skipped over
        parsedIn = inp.split(' ') #seperates input into 3 parts, symbol, direction to go, what symbol to change
        dnaDict[parsedIn[0]] = (parsedIn[1], parsedIn[2])  #WAdd(parsedIn[0],(parsedIn[1], parsedIn[2]))
        if firstLine:
            defaultSym = parsedIn[0]
            firstLine = False





ant = Ant(dnaDict, defaultSym)
currentStep = 0
currentPos = (0,0)
while currentStep < maxSteps:
    currentPos = ant.move(currentPos)
    currentStep+=1
for inp in totalInput:
    print(inp)
print("# {0} {1}\n".format(currentPos[0], currentPos[1]))



