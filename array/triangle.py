class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y
ZERO = 1e-9
def vector_product(vectorA, vectorB):
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y
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
        return False
    else:
        AC = Vector(A, C)
        AD = Vector(A, D)
        BC = Vector(B, C)
        BD = Vector(B, D)
        return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) and (vector_product(AC, BC) * vector_product(AD, BD) <= ZERO)
def checklinetri(point1,point2,triangle2):
        for i in range(0,2):
            for j in range(i+1,3):
                if is_intersected(point1, point2, triangle2[i], triangle2[j]):
                    return True
        return False
def checktritri(triangle1,triangle2):
        for i in range(0,2):
            for j in range(i+1,3):
                if checklinetri(triangle1[i],triangle1[j],triangle2):
                    return True
        return False
n = input()
alldata = []
inter = []
for i in range(0,int(n)):
    inter.append(0)#inter#
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
        if checktritri(alldata[i],alldata[j]):
            inter[i] = 1#==#
            inter[j] = 1
print(inter.count(1))
            
