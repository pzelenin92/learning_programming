def createquery(what,where):
    if where!=None:
        for v in where.values():
            v.append({y:[]})
    else:
        print('There is no '+z+' namespace')

d={'d1':[]}
y,z='level1','d'
createquery(y,d)
