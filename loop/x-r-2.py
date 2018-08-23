n = int(input())
point = []
for i in range(0,n):
    v = []
    v.append(int(input()))
    v.append(int(input()))
    point.append(v)
def key(x):
    return x[0]
point = sorted(point,key = key)
count = point[0][1] - point[0][0]
right = point[0][1]
for i in range(1,n):
    if point[i][1] <= right:
        count = count
        right = right
    elif point[i][0] < right and point[i][1] > right:
        count = count + (point[i][1] - right)
        right = point[i][1]
    elif point[i][0] >= right:
        count = count + (point[i][1] - point[i][0])
        right = point[i][1]
print(count)
