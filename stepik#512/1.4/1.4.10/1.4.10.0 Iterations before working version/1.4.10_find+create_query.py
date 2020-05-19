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

def createquerynew(what,where):
    if where!=None:
        for v in where.values():
            v.append({what:[]})
    else:
        print('There is no '+z+' namespace')

#namespaces={}
#namespaces={'global':[]}
#namespaces={'global':['a','b']}
#namespaces={'global':['a','b',{'level1':[]}]}
#namespaces={'global':['a','b',{'level1':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]}]}
#namespaces={'global':['a','b',{'level2':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]}]}
namespaces={'global':['a','b',{'level1':[{'level4':[]}]},'c',{'level2':[{'level5':[]}]},'d',{'level3':[{'level6':[]}]}]}
y,z='level1','global'
createquerynew(y,findcurrentspace(z,namespaces))


