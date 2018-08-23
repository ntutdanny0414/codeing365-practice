n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)
p = []
v = []
for i in range(1,n+1):
    p.append(i)
now = 0
for i in range(0,k):
    now = (now + m - 1) % len(p)
    v.append(p[now])
    del p[now]
if len(p)==1:
    v.append(p[0])
elif now ==len(p):
    v.append(p[0])
else:
    v.append(p[now])
str1 = ' '.join(str(e) for e in v)
print(str1)

