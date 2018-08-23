from fractions import Fraction
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self,point):
        return self.x == point.x and self.y == point.y
class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y
ZERO = 1e-9
def vector_product(vectorA, vectorB):
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y

def GeneralEquation(a,b):
    A=b.y-a.y
    B=a.x-b.x
    C=b.x*a.y-a.x*b.y
    return A,B,C

def GetIntersectPoint(a,b,c,d):
    A1,B1,C1=GeneralEquation(a,b)
    A2,B2,C2 = GeneralEquation(c,d)
    m=A1*B2-A2*B1
    if a == c and b == d:
        return [[a.x,a.y],[b.x,b.y]]
    elif vector_product(Vector(a,b), Vector(c,d)) == 0:
        v = sorted([[a.x,a.y],[c.x,c.y]])
        if Point(v[0][0],v[0][1]) == a:
            return [[str(c.x),str(c.y)],[str(b.x),str(b.y)]]
        elif Point(v[0][0],v[0][1]) == c:
            return [[str(a.x),str(a.y)],[str(d.x),str(d.y)]]
    else:
        x=Fraction((C2*B1-C1*B2),m)
        y=Fraction((C1*A2-C2*A1),m)
    return [[str(x),str(y)]]
def special_uninter(A, B, C, D):
    v = []
    if A.x == B.x == C.x == D.x:
        v.append([A.y,B.y])
        v.append([C.y,D.y])
        v = sorted(v)
        if v[1][0] > v[0][1]:
            return True
        else:
            return False
    elif vector_product(Vector(A, B), Vector(C, D)) == 0:
        v.append([A.x,B.x])
        v.append([C.x,D.x])
        v = sorted(v)
        if v[1][0] > v[0][1]:
            return True
        else:
            return False

def is_intersected(A, B, C, D):#vector_product==0 sameline#
    if special_uninter(A, B, C, D):
        return []
    else:
        AC = Vector(A, C)
        AD = Vector(A, D)
        BC = Vector(B, C)
        BD = Vector(B, D)
        if (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) and (vector_product(AC, BC) * vector_product(AD, BD) <= ZERO):
            return GetIntersectPoint(A,B,C,D)
        else:
            return []
def checklinetri(point1,point2,triangle2): 
    line = []
    for i in range(0,2):
        for j in range(i+1,3):
            line.extend(is_intersected(point1, point2, triangle2[i], triangle2[j]))
    return line
def checktritri(triangle1,triangle2):
    tri = []
    for i in range(0,2):
        for j in range(i+1,3):
            tri.extend(checklinetri(triangle1[i],triangle1[j],triangle2))
    return tri
n = input()
alldata = []
inter = []#no0#
removerepeat = []
for i in range(0,int(n)):
    triangle = []
    point1 = [int(i) for i in input().split(' ')]
    point2 = [int(i) for i in input().split(' ')]
    point3 = [int(i) for i in input().split(' ')]
    allpoint = sorted([[point1[0],point1[1]],[point2[0],point2[1]],[point3[0],point3[1]]])
    triangle.append(Point(allpoint[0][0],allpoint[0][1]))
    triangle.append(Point(allpoint[1][0],allpoint[1][1]))
    triangle.append(Point(allpoint[2][0],allpoint[2][1]))    
    alldata.append(triangle)
for i in range(0,len(alldata)-1):
    for j in range(i+1,len(alldata)):
        inter.extend(checktritri(alldata[i],alldata[j]))
for i in range(0,len(inter)):
    if inter[i] not in removerepeat:
        removerepeat.append(inter[i])
print(len(removerepeat))
            
