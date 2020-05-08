a='add global a'
b='add global b'
namespaces=dict()
value=[]
x,y,z=a.split()
if x=='add':
    value.append(z)
    namespaces[y]=value
value=[]
x,y,z=b.split()
if x=='add':
    value.append(z)
    namespaces[y]=value
print(namespaces)
