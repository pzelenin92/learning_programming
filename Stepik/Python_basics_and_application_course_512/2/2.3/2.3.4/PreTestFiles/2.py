#попытка заyieldить класс и убрать итерирующаю функцию next, сделав генератор
class MyList:
    def __init__(self, lst):
        self.iterable = lst
#        self.index = 0

    def __iter__(self):
#        while self.index<len(self.iterable):
#            self.index += 1
        for i in self.iterable:
            yield i
#            yield self.iterable[self.index - 1]

"""
    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration
"""
l = MyList([1, 2, 3, 4, 5])
print(list(l))
print(list(l))
