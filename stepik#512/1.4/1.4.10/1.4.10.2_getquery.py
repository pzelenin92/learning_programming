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
                        #if foundspace==False:
                        if valueinspace==None:
                            if type(i) is dict and foundspace is False:
                                upcurrentspace=i
                                getquery(upcurrentspace,y,z)
                            elif i==z and valueoutspace==None and foundspace is True:
                                valueoutspace=currentspace
                        else:
                            break
                    if z in d and valueinspace==None:
                        valueoutspace=currentspace
    getquery(currentspace,y,z)
    if valueinspace!=None:
        return valueinspace
    else:
        return valueoutspace

#namespaces={'global':[]}
#namespaces={'global':['a','b']}
#namespaces={'global':['a',{'level1':['b']}]}
namespaces={'global':['a',{'level1':['b',{'level2':['a']},'c','d']},{'level3':['a']}]}
#namespaces={'global':['b',{'level1':['d',{'level21':['a']},'c']},'a',{'level11':['c']},'c',{'level12':['f']}]}
#namespaces={'global':['a','b',{'level2':[]}]}
#namespaces={'global':['a','b',{'level2':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]}]}
#namespaces={'global':['a','b',{'level1':[{'level4':[]}]},'c',{'level2':[{'level5':[]}]},'d',{'level3':[{'level6':[]}]}]}
y,z='level2','b'
getquery(namespaces,y,z)
