lst_cls = [  # список введённых строк
    'a',
    'b : a',
    'c : a',
    'f : a',
    'd : c b',
    'g : d f',
    'i : g',
    'm : i',
    'n : i',
    'z : i',
    'y : z',
    'x : z',
    'w : e y x'
]
classes={}
for i in lst_cls:
    a,*b=str(i).replace(':',' ').split()
    if a not in classes:
        classes[a]=b
    else:
        classes[a]=classes[a]+b
