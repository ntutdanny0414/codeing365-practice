def getTriangle():
    a,b,c = input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if not a + b > c or not b + c > a or not c + a > b:
        print('1')
    elif a==b==c:
        print('2')
    elif a==b or a==c or b==c: 
        print('3')
    else:
        print('4')
getTriangle()        
