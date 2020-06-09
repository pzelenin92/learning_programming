def fn(x):
    if x in classes:#проверна на наличие в словаре искомого элемента
        lst_checker.add(x)
        for k,v in classes.items():
            if x in v:
                fn(k)
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
    a,*b=str(i).replace(':',' ').split()
    if a not in classes:
        classes[a]=b
    else:
        classes[a]=classes[a]+b
lst_checker=set()
lst_printed=set()
for x in lst_q:
    if x in lst_checker:
        if x not in lst_printed:# проверка на повторные проверки
            lst_printed.add(x)
            print(x)
    else:
        fn(x)
