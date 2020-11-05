import time

class X():
    ''' ciresica are mere'''
    day = time.time()
    seri = []
    lot = []
    def __init__(self, start, nr:int):
        ''' ciresel vine si cere'''
        for i in range(start, start+nr+1):
            self.seri.append(i)
        for i in range (start//20, (start+nr)//20+1):
            self.lot.append(i)
    def __iter__(self):
        return XIter(self.lot)
    def left(self):
        pass
    def right(self):
        pass
class XIter():
    def __init__(self, loturi):
        self.loturi = loturi
    def __iter__(self):
        return self
    def __next__(self):
        if self.loturi:
            return self.loturi.pop(0)
        raise StopIteration
x = X(101, 50)
print(x.seri)
print(x.lot)
for i in x:
    print(i)
