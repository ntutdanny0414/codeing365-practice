#def twototen(data):
#    out = 0
#    power = 0#2^0..2^1#
#    for i in range(len(data)-1,-1,-1):#min in last#
#        if int(i) == 1:#1 need plus#
#            out = out + 2**power
#        power = power + 1#2^2..2^3#
#    return out
def recursion(ten,count = 0):#count cant in function defult0#
    if ten == 0 or ten == 1:
        return count
    elif ten % 2 == 0:#even#
        count = count + 1
        ten = ten / 2
        return recursion(ten,count)#count change#
    elif ten % 2 == 1:
        count = count + 1
        ten = (ten+1) / 2
        return recursion(ten,count)
def tentotwo(ten):
    two = bin(ten)#bin function#
    two = two[2:]#0b1000 remove first 2#
    while len(two) != 4:
        two = '0'+two#ex 7->111 not 0111#
    return two
while True:
    data = input()
    ten = int(data,2)#python way 2 to 10#
    print(tentotwo(recursion(ten)))#dont need give count#
    split = input()
    if split == '-1':
        break
