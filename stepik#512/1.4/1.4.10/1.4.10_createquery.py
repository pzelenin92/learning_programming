def createquery(y,z,currentspace):
    flag1=False
    for v in currentspace.values():
        if len(v)!=0:
                for i in v:
                    if type(i) is dict:
                        if y in i.keys():
                            flag1=False
                        elif z in i.keys():
                            currentspace=i
                            createquery(y,z,i)
                            print('pidor')
                        else:
                            flag1=True
                    else:
                        continue
        else:
            v.append({y:[]})
    if flag1==True:
            v.append({y:[]})

namespaces={'global':['a','b',{'level1':[]}]}
#namespaces={'global':['a','b',{'level2':[]}]}
#namespaces={'global':['a','b',{'level1':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c']}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]}]}
#namespaces={'global':['a','b',{'level2':[]},'c',{'level3':[]},'d',{'level1':[]}]}
#namespaces={'global':['a','b']}
#namespaces={'global':[]}
currentspace=namespaces
createquery('level2','level1',currentspace)
