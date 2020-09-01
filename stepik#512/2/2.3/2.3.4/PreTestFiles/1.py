#попытка отделить итератор от итерирующей функции next в разные классы
class MyIterator:
    def __init__(self, iterable,func,judge):
        self.index = 0
        self.iterable = iterable
        self.func = func
        self.judge = judge
#    def f2(self,n):
#        return n/2
#    def judge(self,num):
#        return"element = "+str(num)

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            self.result_of_f2=self.func(self.iterable[self.index - 1])
            self.result_of_judge=self.judge(self.result_of_f2)
            return self.result_of_judge
        raise StopIteration
class MyList:
    def __init__(self, lst, func,judge):
        self.lst = lst
        self.func = func
        self.judge = judge
    def __iter__(self):
        return MyIterator(self.lst,self.func,self.judge)

def f2(n):
    return n/2
def judge(num):
    return"element = "+str(num)


l = MyList([1, 2, 3, 4, 5],f2,judge)
print(list(l))
print(list(l))
