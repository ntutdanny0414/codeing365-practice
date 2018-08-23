def check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def checkfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def rule1(x):
    if check(x) and 2 <= int(x) <= 1000 and x[0] != '0':#string#
        return True
    else:
        return False

def rule2(x):
    if check(x) and x[0] == '-' and x[1] != '0':
        return True
    else:
        return False

def rule3(x):
    if checkfloat(x) and x.count('.') == 1 and x[0] != '.' and x[-1] != '.'and x[0] != '0'and x[0] != '-' and int(x.split('.')[0]) >= 2:
        return True
    else:
        return False

def rule4(x):
    if checkfloat(x) and x.count('.') == 1 and x[0] == '-' and x[-1] != '.' and int(x.split('.')[1]) >= 2 and len(x.split('.')[0]) >= 2:
        if len(x.split('.')[0]) > 2 and x.split('.')[0][1] == 0:
            return False
        else:
            return True
    else:
        return False

def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i == 0:
            return False
    return True

def maxprime(m,n):
    if isprime(n):
        return n
    elif (n-1)%2 == 0:
        return maxprime(m,n-2)
    else:
        return maxprime(m,n-1)
    
x = input()
if x == '0' or x == '1':
    k = 1000
    print(maxprime(2,k))
elif rule1(x):
    k = int(x)
    print(maxprime(2,k))
elif rule2(x):
    k = int(x)*(-11)
    print(maxprime(2,k))
elif rule3(x):
    k = int(x.split('.')[0])
    print(maxprime(2,k))
elif rule4(x):
    k = int(x.split('.')[1])
    print(maxprime(2,k))
else:
    print('error')
    

