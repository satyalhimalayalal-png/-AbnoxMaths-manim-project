from random import *
list1=[]
while len(list1)<=9:
    new=randint(1,100)
    isduplicate=False
    for x in list1:
        if x==new:
            isduplicate=True
    if not isduplicate:
        list1.append(new)

def bubble():
    global list1
    sorted=False
    upper=len(list1)-1
    while not sorted:
        sorted=True
        for i in range(upper):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
                sorted=False
        upper-=1

def insertion():
    global list1
    for index in range(1,len(list1)):
        sortitem=list1[index]
        correctpos=index
        while correctpos>0 and sortitem<list1[correctpos-1]:
            list1[correctpos]=list1[correctpos-1]
            correctpos-=1
        list1[correctpos]=sortitem


print(list1)
insertion()
print(list1)
            