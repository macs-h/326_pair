

class Ant:

    dna = {}
    plane = {} # key: position, vlaue: if it has been visited the state

    lastPos = 0
    defaultSym = ""
    # Constructor
    def __init__(self, dna, defaultSym):
        self.dna = dna
        self.defaultSym = defaultSym
        self.plane = {}






    def getNewPos(self, dir, currentPos):
        newPos = (0, 0)
        x = 0
        y = 0
        if dir == 'N':
        # moving north
            x = currentPos[0]
            y = currentPos[1] + 1
            self.lastPos = 0

        elif dir == 'E':
            #moving east
            x = currentPos[0] +1
            y = currentPos[1]
            self.lastPos = 1

        elif dir == 'S':
            x = currentPos[0]
            y = currentPos[1] - 1
            self.lastPos = 2

        elif dir == 'W':
            x = currentPos[0] - 1
            y = currentPos[1]
            self.lastPos = 3
        else:
            print("Direction '{}' not valid".format(dir))

        return (x, y)

    def move(self, currentPos):
        nextpos = 'S'
        if currentPos in self.plane:
            #   has already been walked over
            dnaResult = self.dna[self.plane[currentPos]] # dont need to check because plane[currentpos] will onlyreturn valid symbol coz it was set

            nextpos = dnaResult[0][self.lastPos] #where to go next
            self.plane[currentPos] = dnaResult[1][self.lastPos] # changes plane state accordingly

        else :
            #state hasn't been visited before
            dnaResult = self.dna[self.defaultSym]
            nextpos = dnaResult[0][self.lastPos]# where to go next
            self.plane[currentPos] = dnaResult[1][self.lastPos] # changes plane state accordingly

        return self.getNewPos(nextpos, currentPos)

