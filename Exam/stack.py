def initializeStack():
    global stack,headPtr
    stack=[None]*10
    headPtr=-1

def push(item):
    global stack,headPtr
    if headPtr==len(stack)-1:
        print("Stack overflow")
    else:
        headPtr+=1
        stack[headPtr]=item

def pop():
    global stack,headPtr
    if headPtr==-1:
        print("Stack is empty")
    else:
        popitem=stack[headPtr]
        stack[headPtr]=None
        headPtr-=1
        return popitem
def printStackContents():
    global stack,headPtr
    print(f"Stack Contents: {stack} \n headPtr: {headPtr}")
