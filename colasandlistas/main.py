from algo1 import *
from linkedList import *
from stack import*
from queue import*

Q = PriorityQueue()
nodeA = PriorityNode()  
nodeB = PriorityNode() 
nodeC = PriorityNode() 

nodeA.value = 78
nodeB.value = 13
nodeC.value = 1

nodeA.priority = 45
nodeB.priority = 3
nodeC.priority = 0

nodeA.nextNode = nodeB
nodeB.nextNode = nodeC

Q.head = nodeA

print("")
printPriorityQueue(Q)

print (dequeuePriorityQueue(Q))

print("")
printPriorityQueue(Q)
