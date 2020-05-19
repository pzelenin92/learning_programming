def s(a,*vs, b=10):
    res = a+b
    for v in vs:
        res += v
    return res
a1=s(0,0,31)
a2=s(21)
a3=s(11,10,b=10)
a4=s(11,b=20)
a5=s(11,10,10)
#a6=s(b=31) 
#a7=s(b=31,0)
a8=s(11,10)
a9=s(5,5,5,5,1)
print(a1,a2,a3,a4,a5,a8,a9)
