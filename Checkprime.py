num = int(input())
flag=0
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag=1
            break
else:
    flag=1
if(flag==1):
    print('Not Prime')
else:
    print('Prime')
