def gettquery(y,z):#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
    result=None
    def getquery(y,z):
        nonlocal result
        if z in namespaces[y]:
            result=y
        else:
            for i in namespaces[y]:
                if type(i) is dict:
                    y=i['parent']
                    getquery(y,z)
    getquery(y,z)
    return result
