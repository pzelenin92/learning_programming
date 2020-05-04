file=open("inputdictionary.txt","r")
f=file.read().split(';')
f1=[]
for x in f:
    f1.append(x.strip())
while f1.count('')!=0 or f1.count(' ')!=0:
    k=f1.index('')
    del f1[k]
for x in f1:
    print(x)
file.close()
