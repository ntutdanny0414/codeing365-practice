b = int(input())
n = int(input())
v = []
if not 2<=b<=9 or not 0<=n<=10000000:
    print('-1')
else:
    while n!=0:
        out,n = n%b,n//b
        v.append(out)
    v.reverse()
    out = ''.join(str(i) for i in v)
    if len(v) == 0:
        print(0)
    elif int(out) > 100000:
        print('-1')
    else:
        print(''.join(str(i) for i in v))


