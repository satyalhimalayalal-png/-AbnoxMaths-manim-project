from random import randint
def InsertionSort(array):
    for index in range(1,len(array)):
        sortitem=array[index]
        insertPtr=index
        while insertPtr>0 and sortitem<array[insertPtr-1]:
            array[insertPtr]=array[insertPtr-1]
            insertPtr-=1
        array[insertPtr]=sortitem

def GenerateRandomArray():
    list1=[]
    while len(list1)<10:
        isduplicate=False
        new=randint(1,100)
        for element in list1:
            if element==new:
                isduplicate=True
        if not isduplicate:
            list1.append(new)
    return list1

List=GenerateRandomArray()
print(List)
InsertionSort(List)
print(List)