def fibo(n):
    a ,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
check = []
while True:
    x = input()
    if x == '-1':
        break
    elif not x.isdigit():
        check.append('Error')
    elif not 1<=int(x)<=100:##x[0] == 0
        check.append('Error')
    else:
        check.append(fibo(int(x)))
for i in range(0,len(check)):
    print(check[i])
    
