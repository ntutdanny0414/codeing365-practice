import re#lstrip('-')#
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

if len(re.findall(r'\d',x)) == len(x):##
    if x[0] != '0' and 2<=int(x)<=1000:
        k = int(x)
        print(maxprime(2,k))
    elif int(x) == 0 and len(x) == 1:
        k=1000
        print(maxprime(2,k))
    elif x[0] != '0' and int(x)==1:
        k = 1000
        print(maxprime(2,k))
    else:
        print('error')
elif x[0] == '-' and x[1] != '0'and len(re.findall(r'\d',x))+1 == len(x):
    k = int(x)*(-11)
    print(maxprime(2,k))
elif len(re.findall(r'\d',x))+1 == len(x) and len(x.split('.')) == 2:
    if len(x.split('.')[0]) > 1 and x.split('.')[0][0] == '0':
        print('error')
    elif x.split('.')[1] != '' and x.split('.')[0] != '':
        k = int(x.split('.')[0])
        print(maxprime(2,k))
    else:
        print('error')
elif len(x.split('.'))==2 and len(re.findall(r'\d',x))+2 == len(x) and x[0] == '-':
    if len(x.split('.')[0])>2 and x.split('.')[0][1] == '0':
        print('error')
    elif x.split('.')[1] == '' or x.split('.')[0] == '-':
        print('error')
    else:
        k = int(x.split('.')[1])
        print(maxprime(2,k))
else:
    print('error')
    
