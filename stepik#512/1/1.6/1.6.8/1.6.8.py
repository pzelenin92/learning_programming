class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+ self.pop())

    def sub(self):
        self.append(self.pop()- self.pop())

    def mul(self):
        self.append(self.pop()* self.pop())

    def div(self):
        self.append(self.pop()// self.pop())


x=ExtendedStack([1,2,3,4,5])
x.sum()
x.sub()
x.mul()
x.div()
