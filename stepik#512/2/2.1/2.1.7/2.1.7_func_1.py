def fn(x):
    if x in classes:#проверна на наличие в словаре искомого элемента
        lst_checker.add(x)
        for k,v in classes.items():
            if x in v:
                fn(k)
#                lst_checker.add(k)

classes={'a':[],'b' : ['a'],'c' : ['a'],'f' : ['a'],'d' : ['c', 'b'],  'g' : ['d', 'f'],'i' : ['g'],'m' : ['i'],  'n' : ['i'],'z' : ['i'],'e' : ['m', 'n'], 'y' : ['z'],'x' : ['z'],'w' : ['e', 'y', 'x']}
lst_q = ['y','m','n','m','m','d','e','g','a','f']
#classes={'BaseException':[],'Exception' : ['BaseException'],'LookupError' : ['Exception'],'KeyError' : ['LookupError']}
#lst_q = ['BaseException','KeyError']
#classes={'a':[],'b' : ['c','d','a'],'c':[]}
#lst_q = ['a','b']

lst_checker=set()
lst_printed=set()

for x in lst_q:
    if x in lst_checker:
        if x not in lst_printed:# проверка на повторные проверки
            lst_printed.add(x)
            print(x)
    else:
        fn(x)
