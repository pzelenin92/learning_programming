#создать функции для create, add, get
#cсоздать функцию для определения что делать (create,add,get)
#цикл для построчного чтения входных данных
# в неймспейсе должен быть тупль имеющий

#functions
def addquery(y,z):# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    if y in namespaces:
        namespace=namespaces[y]
        namespace.append(z)
    else:
        namespace=[]
        namespace.append(z)
        namespaces[y]=namespace
def createquery(y,z):#create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    namespace=[]
    namespace.append(y)
    namespaces[z]=namespace
def gettquery(y,z):#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
    result=None
    def getquery(y,z):
        nonlocal result
        if z in namespaces[y]:
            result=y
        else:
            for i in namespaces[y]:
                if type(i) is dict:
                    y=i['parent']
                    getquery(y,z)
    getquery(y,z)
    return result
#main
n=int(input())
namespaces=dict()
#i=0
for i in range(n):
    x,y,z=input().split()
    if x=='add':
        addquery(y,z)
    elif x=='create':
        createquery(y,z)
    else:
        print(gettquery(y,z))

#functions
def addquery(y,z):# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    if y in namespaces:
        namespace=namespaces[y]
        namespace.append(z)
    else:
        namespace=[]
        namespace.append(z)
        namespaces[y]=namespace
def createquery(y,z):#create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    namespace=[]
    namespace.append(y)
    namespaces[z]=namespace
def gettquery(y,z):#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
    result=None
    def getquery(y,z):
        nonlocal result
        if z in namespaces[y]:
            result=y
        else:
            for i in namespaces[y]:
                if type(i) is dict:
                    y=i['parent']
                    getquery(y,z)
    getquery(y,z)
    return result
#main
data='add global a\n'\
'create foo global\n'\
'add foo b\n'\
'get foo a\n'\
'get foo c\n'\
'create bar foo\n'\
'add bar a\n'\
'get bar a\n'\
'get bar b'
xdata=data.splitlines()
namespaces=dict()
#i=0
for i in xdata:
    x,y,z=i.split()
    if x=='add':
        addquery(y,z)
    elif x=='create':
        createquery(y,z)
    else:
        print(gettquery(y,z))

"""def createquery(y,z):#create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    if :

        

data='add global a\n'\
'create foo global\n'\
'add foo b\n'\
'get foo a\n'\
'get foo c\n'\
'create bar foo\n'\
'add bar a\n'\
'get bar a\n'\
'get bar b'
xdata=data.splitlines()
namespaces={}
for i in xdata:
    x,y,z=i.split()
    if x=='create':
        createquery(y,z)
"""
"""#functions
def addquery(y,z):# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    if y in namespaces:
        namespace=namespaces[y]
        namespace.append(z)
    else:
        namespace=[]
        namespace.append(z)
        namespaces[y]=namespace
def createquery(y,z):#create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    namespace=[]
    namespace.append(y)
    namespaces[z]=namespace
def gettquery(y,z):#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
    result=None
    def getquery(y,z):
        nonlocal result
        if z in namespaces[y]:
            result=y
        else:
            for i in namespaces[y]:
                if type(i) is dict:
                    y=i['parent']
                    getquery(y,z)
    getquery(y,z)
    return result
#main
data='add global a\n'\
'create foo global\n'\
'add foo b\n'\
'get foo a\n'\
'get foo c\n'\
'create bar foo\n'\
'add bar a\n'\
'get bar a\n'\
'get bar b'
xdata=data.splitlines()
namespaces=dict()
#i=0
for i in xdata:
    x,y,z=i.split()
    if x=='add':
        addquery(y,z)
    elif x=='create':
        createquery(y,z)
    else:
        print(gettquery(y,z))"""
