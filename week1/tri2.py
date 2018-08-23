def compute():
    a,b,c = input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if not a + b > c or not b + c > a or not c + a > b:
        print('Not Triangle')
    elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
        print('Right Triangle')
    elif a*a + b*b < c*c or b*b + c*c < a*a or c*c + a*a < b*b:
        print('Obtuse Triangle')
    else:
        print('Acute Triangle')
compute()        
