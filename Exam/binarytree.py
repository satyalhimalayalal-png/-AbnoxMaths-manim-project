class node:
    def __init__(self,data,rightPtr,leftPtr):
        self.__rightPtr=rightPtr
        self.__leftPtr=leftPtr
        self.__data=data
    def getRightPtr(self):
        return self.__rightPtr
    def getLeftPtr(self):
        return self.__leftPtr
    def getData(self):
        return self.__data
    def setLeftPtr(self,leftPtr):
        self.__leftPtr=leftPtr
    def setRightPtr(self,rightPtr):
        self.__rightPtr=rightPtr
    def setData(self,data):
        self.__data=data

def initialiseBinaryTree():
    global array,rootPtr,freePtr
    array=[node(0,-1,i+1) for i in range(10)]
    array[-1].setLeftPtr(-1)
    rootPtr=-1
    freePtr=0

def addNode(item):
    global array,rootPtr,freePtr
    if freePtr==-1:
        print("BT is full...")
    else:
        newPtr=freePtr
        freePtr=array[freePtr].getLeftPtr()
        array[newPtr].setData(item)
        if rootPtr==-1:
            rootPtr=newPtr
        else:
            curPtr=rootPtr
            while curPtr!=-1:
                if item>array[curPtr].getData():
                    prevPtr=curPtr
                    curPtr=array[curPtr].getRightPtr()
                    direction="R"
                elif item<array[curPtr].getData():
                    prevPtr=curPtr
                    curPtr=array[curPtr].getLeftPtr()
                    direction="L"
            if direction=="L":
                array[prevPtr].setLeftPtr(newPtr)
            elif direction=="R":
                array[prevPtr].setRightPtr(newPtr)
        array[newPtr].setLeftPtr(-1)

def TraverseTree(curPtr):
    global array,rootPtr,freePtr
    if curPtr==-1:
        return
    else:
        TraverseTree(array[curPtr].getLeftPtr())
        print(array[curPtr].getData()) 
        TraverseTree(array[curPtr].getRightPtr())

initialiseBinaryTree()
print(*[array[i].getLeftPtr() for i in range(10)])
TraverseTree(rootPtr)

