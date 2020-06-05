class MoneyBox:
    def __init__(self, capacity):
        self.capacity=capacity
        self.count=0
    def can_add(self, v):
        if self.count+v<=self.capacity:
            return True
        else:
            return False
    def add(self, v):
        if self.can_add(v) is True:
            self.count+=v
