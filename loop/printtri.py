kind = int(input())
line = int(input())
if kind == 1:
    reverse = []
    count = ''
    for i in range(1,int((line+1)/2)+1):
        count = count + str(i)
        print(count)
        reverse.append(count)
    for i in range(len(reverse)-2,-1,-1):
        print(reverse[i])
elif kind == 2:
    re = []
    reverse = []
    for i in range(1,int((line+1)/2)+1):
        re.append('.')
    for i in range(1,int((line+1)/2)+1):
        re[0-i] = str(i)
        string = ''.join(re)
        print(string)
        reverse.append(string)
    for i in range(len(reverse)-2,-1,-1):
        print(reverse[i])
        
        
       