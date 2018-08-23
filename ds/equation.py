from fractions import Fraction
equ = int(input())
data = []
for row in range(equ):
    line = [int(x) for x in input().split()]
    data.append(line)
    
for row in range(len(data)):
    sub = data[row][row]
    for i in range(len(data)):
        if i == row:
            pass#pass#
        else:
            mul = Fraction(data[i][row],sub)#row! sub 0-1-2 to0#
            for j in range(len(data[i])):
                data[i][j] = data[i][j] - data[row][j]*mul
for i in range(len(data)):#frac to string#
    print('X['+str(i+1)+']='+str(data[i][-1]/data[i][i]))#/001122#0+1=1#
