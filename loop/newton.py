def f1_or_f2(function,x,n,c,d):
    if function == 1:
        return x**n - c*(x**(n-2)) - d
    elif function == 2:
        return x**n - c*x - d
def f1d_or_f2d(function,x,n,c,d):
    if function == 1:
        return n*(x**(n-1)) - c*(n-2)*(x**(n-3))
    elif function == 2:
        return n*(x**(n-1)) - c
function = int(input())
n = int(input())
c = float(input())
d = float(input())
err = int(input())
x = d / 2
nextx = 0
while True:
    nextx = x - f1_or_f2(function,x,n,c,d) / f1d_or_f2d(function,x,n,c,d)
    if abs(nextx - x) < 10**(-err):
        break
    else:
        x = nextx
nextx = int(nextx * 10**(err+1)) / 10**(err+1)
print(nextx)
