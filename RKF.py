

class RKF():
    """_summary_
    """
    def __init__(self, function, x0 : float, y0 : float, h : float):
        """_summary_

        Args:
            function (func): The function to solve. Must be in format: myFunction(y, x) -> float
            x0 (float): Initial x value
            y0 (float): Initial y value
            h (float): The h step value
        """
        self.functionMethod = function
        self.x = x0
        self.y = y0
        self.xIN = x0
        self.yIN = y0
        self.h = h
    
    def getK1(self) -> float:
        """Calculate k1

        Returns:
            float: The k1
        """
        return self.functionMethod(self.y, self.x)
    
    def getK2(self) -> float:
        """Calculate k2

        Returns:
            float: The k2
        """
        return self.functionMethod(self.y + (self.h / 2) * self.getK1(), self.x + self.h / 2)
    
    def getK3(self) -> float:
        """Calculate k3

        Returns:
            float: The k3
        """
        return self.functionMethod(self.y + (self.h / 2) * self.getK2(), self.x + self.h / 2)
    
    def getK4(self) -> float:
        """The k4

        Returns:
            float: The k4
        """
        return self.functionMethod(self.y + self.h * self.getK3(), self.x + self.h)
    
    def __iter__(self):
        """Create an Iterator. This runs when the for loop first starts.

        Returns:
            RKF Iterator
        """
        self.x = self.xIN
        self.y = self.yIN
        return self
    
    def __next__(self) -> tuple(float, float):
        """Return the next point estimated.

        Returns:
            tuple(float, float): Returns the next point, in format x, y
        """
        x = self.x + self.h
        weights = self.getK1() + 2 * self.getK2() + 2 * self.getK3() + self.getK4()
        y = self.y + (self.h / 6) * weights
        self.x = x
        self.y = y
        return x, y

def functionIn(y : float, x : float) -> float:
    """An example function passed in

    Args:
        y (float): The y value in
        x (float): The x value in

    Returns:
        float: The value of the function
    """
    return x * x + y

# The RKF object. Set up the initial x and y values. And h value
rkf = RKF(functionIn, x0=0, y0=1, h=0.1)

# Go through the first 100 points.
limit = 100
counter = 0
for result in rkf:
    print(f"X: {result[0]} Y: {result[1]}")
    if(counter >= limit):
        break
    counter += 1
