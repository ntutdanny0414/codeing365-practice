def f1_or_f2(function,x,a):
    if function == 1:
        area = (a - ((x)**2))**0.5
        return abs(area)
    elif function == 2:
        area = ((a * (x**3)) + (7 * x)) / ((a+x)**0.5)
        return abs(area)
def compute_t(h,function,p,q,a,n):
    fp = f1_or_f2(function,p,a)
    fq = f1_or_f2(function,q,a)
    fxi = 0
    i = p + h
    for j in range(0,n-1):
        fxi = fxi + f1_or_f2(function,i,a)
        i = i + h
    return abs((h/2) * (fp + fq + 2*fxi))

i = 1
x = []
number = ''
while True:
    number = input()
    x.append(number)
    if i % 5 == 1 and number == '0':
        break
    else:
        i = i+1
for i in range(0,int((len(x)-1)/5)):
    function = int(x[(i*5)])
    a = int(x[(i*5)+1])
    p = int(x[(i*5)+2])
    q = int(x[(i*5)+3])
    err = int(x[(i*5)+4])
    n0 = 2
    h = (q - p) / n0
    area0 = compute_t(h,function,p,q,a,n0)
    while True:
        n0 = n0 + 20
        h = (q - p) / n0
        area1 = compute_t(h,function,p,q,a,n0)
        k = abs(area1 - area0)
        for i in range(0,err+1):
            k = k * 10
        if k < 10:
            break
        else:
            area0 = area1
    print(round(area1,5))
    
    
    
