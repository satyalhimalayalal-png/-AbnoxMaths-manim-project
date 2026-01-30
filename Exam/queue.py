def initialiseQueue():
    global Q,frontPtr,endPtr
    Q=[None]*10
    frontPtr=-1
    endPtr=-1
def enQ(item):
    global Q,frontPtr,endPtr
    if endPtr==len(Q)-1:
        print("Can't enqueue! Queue is full.")
    else:
        endPtr+=1
        Q[endPtr]=item
        if frontPtr==-1:
            frontPtr=endPtr
def deQ():
    global Q, frontPtr, endPtr
    if frontPtr == -1 or frontPtr > endPtr:
        print("Can't dequeue! Queue is empty.")
    else:
        returnitem = Q[frontPtr]
        frontPtr += 1
        print(f"{returnitem} was dequeued.")
        if frontPtr > endPtr:
            frontPtr = -1
            endPtr = -1
