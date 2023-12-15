def bisect(li,g):
    low=0
    high=len(li)-1
    while low<=high:
        mid=(low+high)//2
        if mid==0 and li[mid]<g:
            break
        elif mid==0:
            return mid
        if li[mid]>=g and li[mid-1]<g:
            return mid
        elif li[mid]>g:
            high=mid
        elif li[mid]<g:
            low=mid+1
    return -1
def allocate(source,g):
    s=[]
    while len(source)>0:
        if bisect(source,g)==-1:
            s.append(source[-1])
            g=g-source[-1]
            source.remove(source[-1])
        elif g>0:
            s.append(source[bisect(source,g)])
            g=0
            source.remove(s[-1])
        else :return s
    return []
start=[int(i) for i in input('enter the number of people in each plane :').split(' ')]
group=[int(i) for i in input('enter the number of people in each group :').split(' ')]
d,r=list(),list()
c=0
t=False
while len(group)!=0:
    d=start.copy()
    for i in group:
        s=allocate(d,i)
        if s!=[]:
            r.append(i)
    for i in r:
        group.remove(i)
    if r==[]:
        t=True
        break
    r=[]
    c+=1
if t==True:
    print('the opitimal time cannot be perdicted')
else:
    print("the optimal time to complete the entire journey is : {0}".format(2*c-1))
   