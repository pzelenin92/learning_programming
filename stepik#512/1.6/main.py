classes={}
l=[]
n=int(input())
for i in range(n):
    z=input().split()
    if len(z)>3:
        for i in range(2,len(z)):
            l.append(z[i])
        classes[z[0]]=l
        l=[]
    elif len(z)==3:
        classes[z[0]]=[z[2]]
    else:
        classes[z[0]]=[]
k=int(input())
for i in range(k):
    x,y=input().split()
    find(x,y)
