def recursion(ten,count = 0):
    if ten == 0 or ten == 1:
        return count
    elif ten % 2 == 0:
        count = count + 1
        ten = ten / 2
        return recursion(ten,count)
    elif ten % 2 == 1:
        count = count + 1
        ten = (ten+1) / 2
        return recursion(ten,count)
def tentotwo(ten):
    two = bin(ten)
    two = two[2:]
    while len(two) != 11:#change 11 output#
        two = '0'+two
    return two
def manytime(ten):#do recur n+1#
    alldata = 0
    for i in range(0,ten+1):#0~n  n+1 time#
        alldata = alldata + recursion(i)#i#
    return alldata#alldata not in for#
while True:
    data = input()
    ten = int(data,2)
    print(tentotwo(manytime(ten)))#many#
    split = input()
    if split == '-1':
        break
