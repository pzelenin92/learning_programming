"Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Пример:
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3.

Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.

Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).

Примечание:
Считать два числа n и k вы можете, например, следующим образом:"

n, k = map(int, input().split())
def cnk(n,k):
    if k==0:
        c=1
        return c    
    elif k>n:
        c=0
        return c    
    else:
        c=cnk(n-1,k)+cnk(n-1,k-1)
        return c    
n,k=map(int,input().split())
a=cnk(n,k)
print(a)
