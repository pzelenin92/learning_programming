#Функция по нахождению нужного namespace
def findcurrentspace(z,currentspace):
    result=None
    def findcurrentspace(z,currentspace):
        nonlocal result
        for v in currentspace:
            if v==z:
                result=currentspace
            else:
                for v in currentspace.values():
                    for i in v:
                        if type(i) is dict:
                            if z in i.keys():
                                result=i
                            else:
                                currentspace=i
                                findcurrentspace(z,currentspace) #уходим на вложенный dict и ищем там
    findcurrentspace(z,currentspace)
    return result

#Функция, которая находит переменную в нужном namespace
def getquery(currentspace,y,z):
    valueinspace=None
    valueoutspace=None
    foundspace=False
    def getquery(currentspace,y,z):
        nonlocal valueinspace
        nonlocal valueoutspace
        nonlocal foundspace
        for d in currentspace:
            if d==y:
                for v in currentspace.values():
                    if z in v:
                        valueinspace=currentspace #переменная внутри искомого namespace
                foundspace=True #ставим метку что дошли до искомого namespace
            else:
                for d in currentspace.values(): #смотрим по значениям в словаре
                    for i in d:
                        if foundspace==False: #сюда заходим если еще не нашли искомого namespace
                            if type(i) is dict:
                                upcurrentspace=i
                                getquery(upcurrentspace,y,z) # уходим на вложенный dict
                        if foundspace==True: # сюда заходим если до этого искомый namespace был найден
                            if valueinspace==None and valueoutspace==None: #если не было переменной в нужном namespace и после выхода из искомого namepsace
                                if z in d:
                                    valueoutspace=currentspace #переменная нашлась после того как дошли до нужного namespace на пути обратно к global
                            break
                    break
    getquery(currentspace,y,z)
    if valueinspace!=None:#распечатываем namespace если переменная искомая была найдена внутри него
        for k in valueinspace.keys():
            print(k)
        return valueinspace
    elif valueoutspace!=None:#распечатываем namespace если переменная искомая была найдена по пути обратно к global
        for k in valueoutspace.keys():
            print(k)
        return valueoutspace
    else:
        print('None')

#Функция добавляет новый namespace в найденный функцией findcurrentspace
def createquery(what,where):
    if where!=None:
        for v in where.values():
            v.append({what:[]})
    else:
        print('There is no '+ z +' namespace')

#Функция добавляет новую перешменную в найденный namespace функцией findcurrentspace
def addquery(what,where):
    if where!=None:
        for v in where.values():
            v.append(what)
    else:
        print('There is no '+ y +' namespace')

#main
namespaces={'global':[]}
n=int(input())
for i in range(n):
    x,y,z=input().split()
    if x=='add':
        addquery(z,findcurrentspace(y,namespaces))
    elif x=='create':
        createquery(y,findcurrentspace(z,namespaces))
    elif x=='get':
        getquery(namespaces,y,z)



