# Тест на то как работает метод reverse()
b=[1,2]

b.reverse()
print(b) #[2, 1]

b.reverse()
print(b) #[1, 2]

x=b.reverse()
print(b) #[2, 1]
print(x) #None

for i in b:
    print(i, end=' ') # 2 1

try:
    for i in x:
        print(i)# TypeError: 'NoneType' object is not iterable
except TypeError:
    print('TypeError: NoneType object is not iterable')


