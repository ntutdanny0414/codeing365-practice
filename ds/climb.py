n = int(input())
s = [1,1,2,4]
if n < len(s):
    print(s[n])
else:
    for i in range(4,n+1):
        s.append(s[i-1]+s[i-2]+s[i-3])

    print(s[len(s)-1])
