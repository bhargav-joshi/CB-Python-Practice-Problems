import math

def primegen(l):
    a=l[0]
    b=l[1]
    for item in range(a,b+1):

        if item<=1:
            pass
        elif item==2 or item==3:
            print(item,end=" ")
            pass
        else:
            flag=1
            for i in range(2,int(math.sqrt(item))+1):
                if item%i==0:
                    flag=0
                    break
                else:
                    flag=1

            if flag==1:
                    print(item,end=" ")
            else:
                    pass

        

t=int(input())


for i in range(0,t):
    l=[int(x) for x in input().split()]
    primegen(l)
    print()
