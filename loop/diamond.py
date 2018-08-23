n = int(input())
plist = []
re = []
for i in range(0,n):
    plist.append('.')
for i in range(1,n+2,2):
    place = int((n-i)/2)
    plist[place] = '*'
    plist[n-1-place] = '*'
    string = ''.join(plist)
    print(string)
    re.append(string)
for i in range(len(re)-2,-1,-1):
    print(re[i])