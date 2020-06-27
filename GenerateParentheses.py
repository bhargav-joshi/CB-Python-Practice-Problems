def gen(openB,closeB,n,s=[]):
    if(closeB==n):
        print(''.join(s))
    else:
        if(openB>closeB):
            s.append(')')
            gen(openB,closeB+1,n,s)
            s.pop()
        if(openB<n):
            s.append('(')
            gen(openB+1,closeB,n,s)
            s.pop()
    return

n = int(input())
gen(0,0,n)
