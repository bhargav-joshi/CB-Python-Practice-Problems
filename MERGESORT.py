def merge(s,e,a=[]):
    mid=(s+e)//2
    i=s
    j=mid+1
    temp=[]
    while(i<=mid and j<=e):
        if(a[i]<a[j]):
            temp.append(a[i])
            i+=1
        else:
            temp.append(a[j])
            j+=1
    while(i<=mid):
        temp.append(a[i])
        i+=1
    while(j<=e):
        temp.append(a[j])
        j+=1
    a[s:e+1]=temp

def mergeSort(s,e,a=[]):
    if(s>=e):
        return
    mid=(s+e)//2
    mergeSort(s,mid,a)
    mergeSort(mid+1,e,a)
    merge(s,e,a)

n=int(input())
a = [i for i in map(int, input().split())]
mergeSort(0,n-1,a)
for i in range(len(a)):
    print(a[i],end=" ")
