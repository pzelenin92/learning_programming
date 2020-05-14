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
                        else:
                            flag1=True
                    else:
                        continue
        else:
            v.append({y:[]})
    if flag1==True:
            v.append({y:[]})
def findcurrentspace(z,currentspace):
    if z in currentspace:
        print('pidor')
    else:
        findcurrentspace(z,
data='create level1 global\ncreate level2 level1\ncreate level3 level2\ncreate level4 level3\n'
xdata=data.splitlines()
namespaces={'global':[]}
currentspace=namespaces
for i in xdata:
    x,y,z=i.split()
    if x=='create':
        findcurrentspace(z,currentspace)
        createquery(y,z,currentspace)
