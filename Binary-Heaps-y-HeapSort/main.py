from algo1 import*
from binary_heap import*
from heap_sort import*

import linkedlist


                

L = linkedlist.LinkedList()
linkedlist.add(L,66)
linkedlist.add(L,72)
linkedlist.add(L,20)
linkedlist.add(L,12)
linkedlist.add(L,47)



linkedlist.printLinkedList(L)
heapsort(L)
print("- - -")
linkedlist.printLinkedList(L)
