from fractions import Fraction

def f1(x1,y1,x2,y2,m,b):
    if x1 - x2 == 0:
        o = 'x='+str(x1)#check1(print_integer(float(x1)))
        print(o)
    elif m == 0:
        o = 'y='+str(y1)
        print(o)
    else:
        o = 'y='+check2(print_integer(m))+'x'+check(print_integer(b))
        print(o)
        
def f2(x1,y1,x2,y2,m1,m2,b1,b2):
    if m2 == 0:
        o = 'x='+str(x1)
        print(o)
    elif m1 == 0:
        o = 'y='+str(y1)
        print(o)
    else:
        o = 'y='+check2(print_fraction(m1,m2))+'x'+check(print_fraction(b1,b2))
        print(o)
    
def print_integer(x):
    if x.is_integer():#only float+-1 0#
        return str(int(x))
    else:
        return str(round(x,2))

def print_fraction(x1,x2):
    x = Fraction(x1, x2)
    return str(x)
    
def check(string):#+-way(week1)#
    if string == '0' or string == '-0':
        return ''
    elif string[0] == '-':
        return string
    else:
        return '+' + string

def check2(string):
    if string == '-1':
         return '-'
    elif string == '1':
         return ''
    else:
        return string#none#
        
point = [int(x) for x in input().split(' ')]#()or' '
x1 = point[0]
y1 = point[1]
x2 = point[2]
y2 = point[3]
m1 = y1 - y2
m2 = x1 - x2
b1 = x2*y1 - x1*y2
b2 = x2 - x1
if m2 == 0 :#x/y y=0#
    m = 0
    b = 0.0
else:
    m = m1 / m2
    b = b1 / b2
if x1 == x2:
    f1(x1,y1,x2,y2,m,b)
elif y1 == y2:
    f1(x1,y1,x2,y2,m,b)
else:
    f1(x1,y1,x2,y2,m,b)
    f2(x1,y1,x2,y2,m1,m2,b1,b2)
