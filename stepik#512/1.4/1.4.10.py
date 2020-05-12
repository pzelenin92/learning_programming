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
def getquery(y,z):#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует

#main
n=int(input())
namespaces=dict()
i=0
while i<n:
    x,y,z=input().split()
    if x=='add':
        addquery(y,z)
        i+=1
    else:
        i+=1
        continue
print(namespaces)

'''namespaces={'global':['a','b','None'],'bar':['c','d',{'parent':'global'}],'foo':['e','f',{'parent':'bar'}]}

if 'a' in namespaces['foo']:
    print('yes')
elif 
    if 'a' in namespaces['bar']:
        print('pidor')

def getquery(y,z):
    if z not in namespaces[y]:'''

'''a='add global a'
b='add global b'
c='add bar a'''''
"""x,y,z=c.split()
addquery(y,z)
print(namespaces)"""
'''value=[]
x,y,z=a.split()
if x=='add':
    value.append(z)
    namespaces[y]=value
value=[]
x,y,z=b.split()
if x=='add':
    value.append(z)
    namespaces[y]=value'''
