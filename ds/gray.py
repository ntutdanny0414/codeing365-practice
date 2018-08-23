def g(n,k):
    if n == 1:
        return str(k)
    elif k < 2**(n-1):
        return '0' + g(n-1, k)
    else:
        return '1' + g(n-1, (2**n)-1-k)
while True:
    data= [int(e) for e in input().split()]
    print(g(data[0],data[1]))
    split = input()
    if split == '-1':
        break

    
