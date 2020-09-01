import itertools
import math
def primes():
    i=1
    while True:
        i+=1
        if (math.factorial(i-1)+1)%i==0:
            yield i
#Простая проверка с помощью генератора
yo = primes()
for i in range(15):
    print (next(yo))
#проверка из условия задачи:
#print(list(itertools.takewhile(lambda x: x <= 31, primes())))
