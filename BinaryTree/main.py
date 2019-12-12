# Bruno Fuentes
# 12401

from math import*
from binarytree import*
from linkedlist import*
from queue import*


"""
PorLaVentana 
yTantosDias 
QuedanAtras 
YaNoMeDuelen 
TodasLasCosas 
QueAyerMe
PodianMolestar
♪♪♪
"""

#vamos a probar con otro arbol
SalgoVoladando=BinaryTree()

A=BinaryTreeNode()
B=BinaryTreeNode()
C=BinaryTreeNode()
D=BinaryTreeNode()
E=BinaryTreeNode()
F=BinaryTreeNode()

A.key=4
A.leftnode=B
A.rightnode=C
A.value="A"

SalgoVoladando.root=A

B.key=2
B.leftnode=D
B.rightnode=E
B.value="B"
B.parent=A

C.key=8
C.rightnode=F
C.value="C"
C.parent=A

D.key=1
D.value="D"
D.parent=B

E.key=3
E.value="E"
E.parent=B

F.key=9
F.value="F"
F.parent=C


################
#  RECORRIDOS  #
################
print("Pre order:")
traverseInPreOrder(SalgoVoladando)
print("In order:")
traverseInOrder(SalgoVoladando)
print("Post order:")
traverseInPostOrder(SalgoVoladando)
print("Amplitud:")
traverseBreadFirst(SalgoVoladando)


#################
#  OPERACIONES  #
#################
print("Insert:")
insertB(SalgoVoladando,"G",20)
traverseBreadFirst(SalgoVoladando)

print("Search:")
print (searchB(SalgoVoladando,"G"))

print("Access:")
print(accessB(SalgoVoladando,15))


print("Update:")
updateB(SalgoVoladando,"GG",20)
traverseBreadFirst(SalgoVoladando)


print("Se agregan 2 nodos,'H' e 'I'")
insertB(SalgoVoladando,"H",15)
insertB(SalgoVoladando,"I",25)
traverseBreadFirst(SalgoVoladando)
print("Se agregan 2 nodos,'J' e 'K'")
print("Que son hijos de H")
insertB(SalgoVoladando,"J",13)
insertB(SalgoVoladando,"K",16)
traverseBreadFirst(SalgoVoladando)


print("Delete Key:")
deleteKey(SalgoVoladando,4)
traverseBreadFirst(SalgoVoladando)
"""
print("Delete Key:")
deleteKey(SalgoVoladando,3)
traverseBreadFirst(SalgoVoladando)
"""



print("Delete Element:")
deleteB(SalgoVoladando,"E")
traverseBreadFirst(SalgoVoladando)


# URL: 
                                                                            