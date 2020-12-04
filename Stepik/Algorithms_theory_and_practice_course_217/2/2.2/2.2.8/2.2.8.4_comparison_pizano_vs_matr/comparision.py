import timeit

n,m=9,2
t1=timeit.timeit('pizano.fib_mod(n, m)', setup='import pizano',globals=globals())
t2=timeit.timeit('matr.fib_mod(n, m)', setup='import matr',globals=globals())

print('t1=',t1,'\nt2=',t2)
