def initialiseQueue():
    global Q, frontPtr, endPtr, numOfItems
    Q = [None] * 10
    frontPtr = -1
    endPtr = -1
    numOfItems = 0

def enQ(item):
    global Q, frontPtr, endPtr, numOfItems
    if numOfItems == len(Q):
        print("Can't enqueue! Queue is full.")
    else:
        if numOfItems == 0:
            frontPtr = 0
        endPtr = (endPtr + 1) % len(Q)
        Q[endPtr] = item
        numOfItems += 1
def deQ():
    global Q, frontPtr, endPtr, numOfItems
    if numOfItems == 0:
        print("Can't dequeue! Queue is empty.")
    else:
        returnitem = Q[frontPtr]
        Q[frontPtr] = None
        frontPtr = (frontPtr + 1) % len(Q)
        numOfItems -= 1
        if numOfItems == 0:  # reset pointers when queue becomes empty
            frontPtr = -1
            endPtr = -1
        return returnitem