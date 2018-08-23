import math
a,b,c,d,e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
u = float(a+b+c+d+e)/5.0
u2 = float(a*a+b*b+c*c+d*d+e*e)/5.0
var = u2 - u*u
d = math.sqrt(var)
print('{:.2f}'.format(u))
print('{:.2f}'.format(var))
print('{:.2f}'.format(d))
