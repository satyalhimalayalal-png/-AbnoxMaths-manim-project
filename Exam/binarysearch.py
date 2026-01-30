# class node:
#     def __init__(self,left,data,right):
#         self.__leftpointer=left
#         self.__data=data
#         self.__rightpointer=right
#     def getLeftPtr(self):
#         return self.__leftpointer
#     def getRightPtr(self):
#         return self.__rightpointer
#     def getData(self):
#         return self.__data
#     def setLeftPtr(self,left):
#         self.__leftpointer=left
#     def setRightPtr(self,right):
#         self.__rightpointer=right
#     def setData(self,data):
#         self.__data=data

# def initializeBinaryTree():
#     global tree,rootPtr,freePtr
#     freePtr=0
#     rootPtr=-1
#     tree=[node(i+1,0,-1) for i in range(10)]
#     tree[-1].setLeftPtr(-1)

# def addNode(data):
#     global tree,rootPtr,freePtr
#     if freePtr==-1:
#         print("Tree is full")
#     else:
#         newNodePtr=freePtr
#         tree[newNodePtr].setData(data)
#         freePtr=tree[newNodePtr].getLeftPtr()
#         tree[newNodePtr].setLeftPtr(-1)
#         if rootPtr==-1:
#             rootPtr=newNodePtr
#         else:
#             curPtr=rootPtr
#             while curPtr!=-1:
#                 prevPtr=curPtr
#                 if data>tree[curPtr].getData():
#                     curPtr=tree[curPtr].getRightPtr()
#                     directionLeft=False
#                 elif data<tree[curPtr].getData():
#                     curPtr=tree[curPtr].getLeftPtr()
#                     directionLeft=True
#                 elif data==tree[curPtr].getData():
#                     print("Data to add is already present in tree. Cannot duplicate...")
#                     return
#             if directionLeft:
#                 tree[prevPtr].setLeftPtr(newNodePtr)
#             else:
#                 tree[prevPtr].setRightPtr(newNodePtr)

# def inTraversal(curPtr):
#     global tree
#     if curPtr==-1:
#         return
#     inTraversal(tree[curPtr].getLeftPtr())
#     print(tree[curPtr].getData(),end=" ")
#     inTraversal(tree[curPtr].getRightPtr())

# def preTraversal(curPtr):
#     global tree
#     if curPtr==-1:
#         return
#     print(tree[curPtr].getData(),end=" ")
#     preTraversal(tree[curPtr].getLeftPtr())
#     preTraversal(tree[curPtr].getRightPtr())

# def postTraversal(curPtr):
#     global tree
#     if curPtr==-1:
#         return
#     postTraversal(tree[curPtr].getLeftPtr())
#     postTraversal(tree[curPtr].getRightPtr())
#     print(tree[curPtr].getData(),end=" ")

# def searchTree(searchItem):
#     global tree,rootPtr
#     searchPtr=rootPtr
#     found=False
#     while searchPtr!=-1 and not found:
#         if searchItem>tree[searchPtr].getData():
#             searchPtr=tree[searchPtr].getRightPtr()
#         elif searchItem<tree[searchPtr].getData():
#             searchPtr=tree[searchPtr].getLeftPtr()
#         elif searchItem==tree[searchPtr].getData():
#             found=True
#     if found:
#         return searchPtr
#     else:
#         return -1

# # Override the global tree with a custom expression tree
# initializeBinaryTree()

# # Manually assign nodes for: (3 + (4 * 5))
# # tree[0] = '+'
# # tree[1] = '3'
# # tree[2] = '*'
# # tree[3] = '4'
# # tree[4] = '5'

# tree[0] = node(1, '+', 2)
# tree[1] = node(-1, '3', -1)
# tree[2] = node(3, '*', 4)
# tree[3] = node(-1, '4', -1)
# tree[4] = node(-1, '5', -1)

# rootPtr = 0  # root is '+'

# print("Infix expression (Standard notation):")
# inTraversal(rootPtr)  # Expected: 3 + 4 * 5

# print("\nPrefix expression (Polish notation):")
# preTraversal(rootPtr)  # Expected: + 3 * 4 5

# print("\nPostfix expression (Reverse Polish notation):")
# postTraversal(rootPtr)  # Expected: 3 4 5 * +

