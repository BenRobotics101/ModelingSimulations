

class RKF():
    def __init__(self, function, x0, y0, h):
        self.functionMethod = function
        self.x = x0
        self.y = y0
        self.xIN = x0
        self.yIN = y0
        self.h = h
    
    def getK1(self):
        return self.functionMethod(self.y, self.x)
    
    def getK2(self):
        return self.functionMethod(self.y + (self.h / 2) * self.getK1(), self.x + self.h / 2)
    
    def getK3(self):
        return self.functionMethod(self.y + (self.h / 2) * self.getK2(), self.x + self.h / 2)
    
    def getK4(self):
        return self.functionMethod(self.y + self.h * self.getK3(), self.x + self.h)
    
    def __iter__(self):
        self.x = self.xIN
        self.y = self.yIN
        return self
    
    def __next__(self):
        x = self.x + self.h
        weights = self.getK1() + 2 * self.getK2() + 2 * self.getK3() + self.getK4()
        y = self.y + (self.h / 6) * weights
        self.x = x
        self.y = y
        return x, y

def functionIn(y, x):
    return x * x + y

rkf = RKF(functionIn,x0=0,y0=1,h=0.1)

limit = 100
counter = 0
for result in rkf:
    print(f"X: {result[0]} Y: {result[1]}")
    if(counter >= limit):
        break
    counter += 1
