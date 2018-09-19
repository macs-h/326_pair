# Python program to detect cycle 
# in a graph
 
from functools import reduce
from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
 

def factors(n):
    setOfFactors = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    setOfFactors.remove(n)
    return setOfFactors


#TODO: For each number from 1 -> 9,000,000, find any loops

loop_nums = []
next_num = 0
original = 1264460
count = 0
g = Graph(14)
while count < 15:
    if count == 0:
        next_num = original
        g.addEdge(original, next_num)
        print("Starting:", next_num)
    count+= 1

    t = factors(next_num)
    print(t)
    prev_num = next_num
    next_num = sum(t)
    g.addEdge(prev_num, next_num)
    print("Next:", next_num)


# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
if g.isCyclic() == 1:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")