n = int(input())
v = input()
v = v.split(' ')
matrix=[]
for i in range(0,n):
    matrix.append([])
for i in range(0,n):
    for j in range(1,n+1):
        matrix[i].append(n*i+j)
for i in v:
    if i == 'R':
        matrix[:] = map(list,zip(*matrix[::-1]))
    elif i == 'L':
        matrix[:] = map(list,zip(*matrix))
        matrix[:] = matrix[::-1]
    elif i == 'N':
        matrix[:] = matrix[::-1]
    elif i == 'F':
        pass

#matrix[:] = map(list,zip(*matrix[::-1]))
#matrix[:] = map(list,zip(*matrix))
#matrix[:] = matrix[::-1]
#matrix[:] = map(list,zip(*matrix))
for i in range(0,n):
    str1 = ' '.join(str(e) for e in matrix[i])
    print(str1)
