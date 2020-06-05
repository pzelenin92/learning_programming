def fn(x,i):
    finded=False
    def fn(x,i):
        nonlocal finded
        if x in classes: # если есть искомый x в classes
            if classes[x] in lst_q[:i]:
                finded=True
            else:
                fn(classes[x],i)
    fn(x,i)
    if finded==True:
        print(x)
n=int(input())
lst_cls=[]
for i in range(n):
    lst_cls.append(input())
m=int(input())
lst_q=[]
for i in range(m):
    lst_q.append(input())
classes={}
for i in lst_cls:
    x=str(i).replace(':',' ').split()
    if len(x)==1:
        classes[i]=None
    else:
        a,b=x[0],x[1]
        classes[a]=b
for x in lst_q:
    fn(x,lst_q.index(x))
