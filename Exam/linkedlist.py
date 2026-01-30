def initializeLinkedList():
    global list1, headPtr,freePtr,nullptr
    list1=[[0,i+1] for i in range(10)]
    list1[-1][1]=-1
    nullptr=-1
    freePtr=0
    headPtr=nullptr

def addNode(addItem):
    global list1, headPtr,freePtr,nullptr
    if freePtr==nullptr:
        print("List is full, cannot add a new node...")
    else: 
        list1[freePtr][0]=addItem
        curPtr=headPtr
        newNodePtr=freePtr
        freePtr=list1[freePtr][1]
        while curPtr!=nullptr and addItem>list1[curPtr][0]:
            prevPtr=curPtr
            curPtr=list1[curPtr][1]
        if curPtr==headPtr:
            headPtr=newNodePtr
        else:
            list1[prevPtr][1]=newNodePtr
        list1[newNodePtr][1]=curPtr

def removeNode(removeItem):
    global list1, headPtr,freePtr,nullptr
    if headPtr==nullptr:
        print("List is empty, no node to remove...")
    else: 
        curPtr=headPtr
        prevPtr=nullptr
        while curPtr!=nullptr and removeItem!=list1[curPtr][0]:
            prevPtr=curPtr
            curPtr=list1[curPtr][1]
        if curPtr==nullptr:
            print("Item to remove not found...")
            return
        list1[curPtr][0]=0
        list1[curPtr][1]=freePtr
        freePtr=curPtr
        if curPtr==headPtr:
            headPtr=list1[curPtr][1]
        else:
            list1[prevPtr][1]=list1[curPtr][1]

    

initializeLinkedList()

def displayLinkedList():
    global list1, headPtr, nullptr
    curPtr = headPtr
    print("Linked List: ", end="")
    while curPtr != nullptr:
        print(f"[{list1[curPtr][0]}|{list1[curPtr][1]}] -> ", end="")
        curPtr = list1[curPtr][1]
    print("None")

while True:
    print("\nMenu:")
    print("1. Add node")
    print("2. Remove node")
    print("3. Display linked list")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = float(input("Enter item to add to linked list: "))
        addNode(item)
    elif choice == "2":
        item = float(input("Enter item to remove from linked list: "))
        removeNode(item)
    elif choice == "3":
        displayLinkedList()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")