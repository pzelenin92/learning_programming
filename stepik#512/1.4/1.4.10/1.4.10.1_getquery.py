def getquery(currentspace,y,z):
    result=None
    flag=None
    def getquery(currentspace,y,z):
        nonlocal result
        nonlocal flag
        for d in currentspace:
            if d==y:
                for v in currentspace.values():
                    if z in v:
                        result=currentspace
            else:
                for d in currentspace.values():
                    for i in d:
                        if result==None:
                            if type(i) is dict:
                                currentspace=i
                                getquery(currentspace,y,z)
                            elif i==z:
                                flag=currentspace
                        else:
                            break

#                           if z in i.keys():
#                               result=i
#                           else:
#                               currentspace=i
#                               findcurrentspace(currentspace,y,z)
    getquery(currentspace,y,z)
    if result!=None:
        return result
    else:
        return flag

#namespaces={'global':[]}
#namespaces={'global':['a','b']}
#namespaces={'global':['a','b',{'level1':[]}]}
namespaces={'global':['a',{'level1':['d',{'level21':['a1']}]},'b',{'level11':['e']},'c',{'level12':['f']}]}
#namespaces={'global':['a','b',{'level2':[]}]}
#namespaces={'global':['a','b',{'level2':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]}]}
#namespaces={'global':['a','b',{'level1':[{'level4':[]}]},'c',{'level2':[{'level5':[]}]},'d',{'level3':[{'level6':[]}]}]}
y,z='level21','d'
getquery(namespaces,y,z)
