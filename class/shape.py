class Shape:
    def __init__(self,x,y):##not int
        self.x = x
        self.y = y
    def len(self):
        return 2 * (self.x + self.y)
    def area(self):
        return self.x * self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def len(self):
        return 2 * 4 * self.radius
    def area(self):
        return self.radius * self.radius * 4
class Rectangle(Shape):
    def __init__(self,lenth,width):
        self.lenth = lenth
        self.width = width
    def len(self):
        return 2 * (self.lenth+ self.width)
    def area(self):
        return self.lenth * self.width
class Square(Shape):
    def __init__(self,lenth):
        self.lenth = lenth
    def len(self):
        return 4 * self.lenth
    def area(self):
        return self.lenth * self.lenth
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def len(self):
        return self.a + self.b + self.c#self.#
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return round(area,3)
n = int(input())
alllen = []
for i in range(0,n):
    data = input().split()#string to int#
    if data[0] == 'C':
        alllen.append(Circle(int(data[1])).len())
    elif data[0] == 'R':
        alllen.append(Rectangle(int(data[1]),int(data[2])).len())
    elif data[0] == 'S':
        alllen.append(Square(int(data[1])).len())
    elif data[0] == 'T':
        alllen.append(Triangle(int(data[1]),int(data[2]),int(data[3])).len())
for i in range(0,len(alllen)):
    print(alllen[i])
print(sum(alllen))
