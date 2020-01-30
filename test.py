def search1():
    l1=[]
    no=int(input("enter the  no of elements in t list"))
    for i in range(0,no):
        el=input("enter the next element")
        l1.append(el)

    p=input("enter no to b searched")
    for i in range(0,len(l1)):
        if l1[i]==p:
            return (print("element found at location",i+1))
            break

    if i==len(l1):
        return -1
#k=search1()

def rotate():

    l1 = []
    no = int(input("enter the  no of elements in t list"))
    for i in range(0, no):
        el = input("enter the next element")
        l1.append(el)
    p=int(input("enter no of times "))
    if p>no:
        print("invalid entry")
    else:
        for i in range(0,no):
            print(l1[-p+i])
#rotate()


def  countdivisor(a,b,c):
    count=0
    for i in range(a,b+1):
        if i%c==0:
            count=count+1
    print(count)
#countdivisor(10,30,6)

def largodd(a,b,c):
    if(a > b) & (a > c) & (a % 2 == 1):
        print(a)
    if(b > a) & (b > c) & (b % 2 == 1):
        print(b)
    if(c > b) & (c > a) & (c % 2 == 1):
        print(c)
#largodd(2,3,5)



def list1():
    l1=[]
    sum=0
    no=int(input("enter the  no of elements in t list"))
    for i in range(0,no):
        el=float(input("enter the next element"))
        l1.append(el)
    for i in range(0,no):
        sum=sum+l1[i]
    print("the sum is",sum)
#list1()





