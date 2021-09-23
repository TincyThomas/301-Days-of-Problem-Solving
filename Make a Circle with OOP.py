class Rectangle:

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)


class Circle:
	def __init__(self, radi = 0):
		self.radi = radi

	def getArea(self):
		return (22/7)*self.radi * self.radi

	def getPerimeter(self):
		return 2*(22/7) * self.radi
circy = Circle(11)
print(circy.getArea())
