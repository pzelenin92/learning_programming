lst_cls = [  # список введённых строк
'A',
'B',
'C',
'D',
'E : B',
'F : B',
'G : B',
'H : C',
'I : C',
'J : C',
'K : H',
'L : H',
'M : H',
'N : D',
'O : D',
'P : D',
'R : N',
'S : N',
'T : N',
'U : R',
'V : R',
'W : R',
]
classes={}
for i in lst_cls:
    x=str(i).replace(':',' ').split()
    if len(x)==1:
        classes[i]=None
    else:
        a,b=x[0],x[1]
        classes[a]=b
