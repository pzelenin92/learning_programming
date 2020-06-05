def find(x,y):
    finded=False
    def find(x,y):
        nonlocal finded
        if y in classes:#проверка на наличие стартового класса в словаре с классами
            if x==y: # если такой класс есть в словаре, то проверяем на равенство
               print('Yes')
               finded=True
               return # если они равны значит выходим из функции с принтом yes
            if x in classes[y]:# если классы не равны, то проверяем есть ли внутри листа искомый класс x
                print('Yes')
                finded=True
            else: # если классы не равны то проверка внутри листа поэлементно
                for i in classes[y]:
                    if finded==False:# условние нужно чтобы не проверять дальше по элементам в списке, если нашли искомый класс
                         find(x,i)
                    else:
                        return
    find(x,y)
    if finded==False:
        print('No')
classes={
'A':[],
'B' : [],
'C' : [],
'D' : [],
'E' : ['B'],
'F' : ['B'],
'G' : ['B'],
'H' : ['C'],
'I' : ['C'],
'J' : ['C'],
'K' : ['H'],
'L' : ['H'],
'M' : ['H'],
'N' : ['D'],
'O' : ['D'],
'P' : ['D'],
'R' : ['N'],
'S' : ['N'],
'T' : ['N'],
'U' : ['R'],
'V' : ['R'],
'W' : ['R'],
}

lst_q = [
'A',
'E',
'F',
'B',
'G', #print
'H'
'K',#print
'L',#print
'I',
'C',
'J',#print
'U',
'V',
'N',
'W',#print
'R',#print
'S',#print
'T',#print
'O',
'D',
'P'#print
]

for i in lst_q:
    x,y=str(i).split()
    find(x,y)
