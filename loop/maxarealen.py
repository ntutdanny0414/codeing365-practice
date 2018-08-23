def compute(x1,y1,x2,y2):
    lenth = abs(x2-x1)
    width = abs(y2-y1)
    perimeter = 2 * (lenth + width)
    area = lenth * width
    return [area,perimeter]

outcome = [0,0]

while True :
    data = [int(i) for i in input().split()]
    if data[0] == -1:
        break
    else:
        if compute(data[0],data[1],data[2],data[3])[0] > outcome[0]:
            outcome[0] = compute(data[0],data[1],data[2],data[3])[0]
        if compute(data[0],data[1],data[2],data[3])[1] > outcome[1]:
            outcome[1] = compute(data[0],data[1],data[2],data[3])[1]
for i in range(0,2):
    print(outcome[i])
    
