def smallrange(x):
    if x // 3 == 0:
        return [0,3]
    elif x // 3 == 1:
        return [3,6]
    elif x // 3 == 2:
        return [6,9]
def notin(rule):
    notin = []
    for i in range(1,10):
        if i not in rule:
            notin.append(i)
    return notin
def check(i,j,data):
    rule1 = data[i]
    rule2 = []
    rule3 = []
    smalli = smallrange(i)
    smallj = smallrange(j)
    for i in range(0,len(data)):
        rule2.append(data[i][j])
    for x in range(smalli[0],smalli[1]):
        for y in range(smallj[0],smallj[1]):
            rule3.append(data[x][y])
    return set(notin(rule1))&set(notin(rule2))&set(notin(rule3))
def find0(data):
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):#row len different?#
            if data[i][j] == 0:
                print(i,j,check(i,j,data).pop())
def main():                
    sukodu = []
    for i in range(0,9):
        string = input()
        row = []
        for j in range(0,len(string)):
            row.append(int(string[j]))
        sukodu.append(row)
    find0(sukodu)
main()