s, a, b = (input() for k in range(3))
i=0
while a in s and i<=1000:
    s=s.replace(a,b)
    i+=1
if i<=1000:
    print(i)
else:
    print('Impossible')
