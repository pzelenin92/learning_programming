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
                                findcurrentspace(z,currentspace)
    findcurrentspace(z,currentspace)
    return result

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
                        valueinspace=currentspace
                foundspace=True
            else:
                for d in currentspace.values():
                    for i in d:
                        if valueinspace==None:
                            if type(i) is dict and foundspace is False:
                                upcurrentspace=i
                                getquery(upcurrentspace,y,z)
                            elif i==z and valueoutspace==None and foundspace is True:
                                valueoutspace=currentspace
                        else:
                            break
    getquery(currentspace,y,z)
    if valueinspace!=None:
        return valueinspace
    else:
        return valueoutspace

def createquery(what,where):
    if where!=None:
        for v in where.values():
            v.append({what:[]})
    else:
        print('There is no '+ z +' namespace')

def addquery(what,where):
    if where!=None:
        for v in where.values():
            v.append(what)
    else:
        print('There is no '+ y +' namespace')

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
namespaces={'global':[]}
for i in xdata:
    x,y,z=i.split()
    if x=='add':
        addquery(z,findcurrentspace(y,namespaces))
    elif x=='create':
        createquery(y,findcurrentspace(z,namespaces))
    else:
        print(getquery(namespaces,y,z))

#namespaces={}
#namespaces={'global':[]}
#namespaces={'global':['a','b']}
#namespaces={'global':['a','b',{'level1':[]}]}
#namespaces={'global':['a','b',{'level1':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]}]}
#namespaces={'global':['a','b',{'level2':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]}]}
#namespaces={'global':['a','b',{'level1':[{'level4':[]}]},'c',{'level2':[{'level5':[]}]},'d',{'level3':[{'level6':[]}]}]}



