import math

def pythagorean(c):
    for a in range(int(math.sqrt(c))+1):
        b = math.sqrt(c - (a ** 2)) 
        if b == int(b) and a <=int(b):
            print("({},{})".format(a,int(b)), end=" ")

t = int(input())

arr = []

for _ in range(t):
    n= int(input())
    arr.append(n)

for i in arr:
    pythagorean(i)
    print()
