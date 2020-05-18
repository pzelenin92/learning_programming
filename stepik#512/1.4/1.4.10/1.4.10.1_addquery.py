def addquery(what,where):
    if where!=None:
        for v in where.values():
            v.append(what)
    else:
        print('There is no '+ y +' namespace')
