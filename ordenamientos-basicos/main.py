from linkedlist import*
from basic_sort import*


L = LinkedList()
add(L,2)
add(L,5)
add(L,3)
add(L,1)
add(L,4)

printLinkedList(L)

print("·Insertion Sort·")
# bubblesort(L)
# selectionsort(L)
insertionsort(L)
print("···")
printLinkedList(L)  






