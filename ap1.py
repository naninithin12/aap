def findmax(a,b,c):
    if a<b and c<b:
        return b
    elif a<c and b<c:
        return c
    else:
        return a

def MaxSum(a,n):
    msum=float('-inf')
    c=1
    li=[]
    for i in range(n):
        x=msum
        msum=findmax(a[i],msum+a[i],msum)
        if (msum>x and msum>=0) or a[i]==0:
            c+=1
            li.append(a[i])
        elif msum>x and msum !=x:
            li=[a[i]]
    return (msum,c,li) if msum<0 else (msum,c-1,li)
n=int(input('Enter no.of elements :'))
li=[]
for i in range(n):
    li.append(int(input('Enter the element :')))
msum,c,li=MaxSum(li,n)
print('Maximum sum of subset is {0} With the maximum elements {1}'.format(msum,c))
if len(li)!=c:
    li=li[1:]
print(li)