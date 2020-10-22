def fn(x,i):
    finded=False
    def fn(x,i):
        nonlocal finded
        if x in classes: # если есть искомый x в classes
            if classes[x] in lst_q[:i]:
                finded=True
            else:
                fn(classes[x],i)
    fn(x,i)
    if finded==True:
        print(x)

classes={
'A':None,
'B' :None,
'C' :None,
'D' :None,
'E' : 'B',
'F' : 'B',
'G' : 'B',
'H' : 'C',
'I' : 'C',
'J' : 'C',
'K' : 'H',
'L' : 'H',
'M' : 'H',
'N' : 'D',
'O' : 'D',
'P' : 'D',
'R' : 'N',
'S' : 'N',
'T' : 'N',
'U' : 'R',
'V' : 'R',
'W' : 'R',
}

lst_q = [
'A',
'E',
'F',
'B',
'G',#print
'H',
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

for x in lst_q:
    fn(x,lst_q.index(x))
