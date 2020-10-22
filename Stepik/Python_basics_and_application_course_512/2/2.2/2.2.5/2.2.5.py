from datetime import date
from datetime import timedelta
l=[int(i) for i in input().split()]
x=date(*l)
y=timedelta(int(input()))
c=x+y
print(c.year,c.month,c.day)
