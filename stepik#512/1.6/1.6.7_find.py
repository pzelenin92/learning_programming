classes={'a':[],'b':['a'],'c':[],'d':['b'],'e':['c','d']}
x,y='a','e'
def find(x,y):
    finded=False
    def find(x,y):
        nonlocal finded
        if y in classes:
            if x in classes[y]:
                print('Yes')
                finded=True
#                return 'Yes'
            else:
                for i in classes[y]:
                    if finded==False:
                         find(x,i)
                    else:
                        return
#        else:
#            print('Нет такого элемента в словаре')
    find(x,y)
    if finded==False:
        print('No')
find(x,y)
