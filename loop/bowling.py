score = []
fun = []
count = 0
for i in range(0,10):
    s1 = int(input())
    s2 = int(input())
    if s1 == 10:
        score.append([s1,s2])
        fun.append('x')
    elif s1 + s2 == 10:
        score.append([s1,s2])
        fun.append('/')
    else:
        score.append([s1,s2])
        fun.append(' ')

for i in range(0,8):
    if fun[i] == 'x':
        if fun[i+1] == 'x':
            count = count + score[i][0] + score[i+1][0] + score[i+2][0]
        else:
            count = count + score[i][0] + score[i+1][0] + score[i+1][1]
    elif fun[i] == '/':
        count = count + score[i][0] + score[i][1] + score[i+1][0]
    else:
        count = count + score[i][0] + score[i][1]
if score[8][0] == 10:
    count = count + 10 + score[9][0] + score[9][1]
elif score[8][0] + score[8][1]== 10:
    count = count + 10 + score[9][0]
else:
    count = count + score[8][0] + score[8][1]

if score[9][0] == 10 or score[9][0] + score[9][1] == 10:
    last = int(input())
    count = count + score[9][0] + score[9][1] + last
else:
    last = int(input())
    count = count + score[9][0] + score[9][1]
print(count)
    
