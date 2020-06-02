def find(x,y):
    finded=False
    def find(x,y):
        nonlocal finded
        if y in classes:#проверка на наличие стартового класса в словаре с классами
            if x==y: # если такой класс есть в словаре, то проверяем на равенство
               print('Yes')
               finded=True
               return # если они равны значит выходим из функции с принтом yes
            if x in classes[y]:# если классы не равны, то проверяем есть ли внутри листа искомый класс x
                print('Yes')
                finded=True
            else: # если классы не равны то проверка внутри листа поэлементно
                for i in classes[y]:
                    if finded==False:# условние нужно чтобы не проверять дальше по элементам в списке, если нашли искомый класс
                         find(x,i)
                    else:
                        return
    find(x,y)
    if finded==False:
        print('No')
#собираем зависимости между классами в лист для последующей обработки
n=int(input())
lst_cls=[]
for i in range(n):
    lst_cls.append(input())
#собираем запросы в лист для последующей обработки
m=int(input())
lst_q=[]
for i in range(m):
    lst_q.append(input())
classes={}
#делаем словарь с классовыми зависимостями из листа lst_cls
for i in lst_cls:
    a,*b=str(i).replace(':',' ').split()
    if a not in classes:
        classes[a]=b
    else:
        classes[a]=classes[a]+b
#обрабатываем лист запросов lst_q функцией find
for i in lst_q:
    x,y=str(i).split()
    find(x,y)

