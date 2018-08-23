x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
choose = 0
count = 0
count1 = x1*0.08+x2*0.139+x3*0.135+x4*1.128+x5*1.483
count2 = x1*0.07+x2*0.130+x3*0.121+x4*1.128+x5*1.483
count3 = x1*0.06+x2*0.108+x3*0.101+x4*1.128+x5*1.483
if count1 <= 183:
    choose = 183
    count = 183
elif 183 < count1 < 383:
    choose = 183
    count = count1
elif 983 > count1 >= 383 and count2 <= 383:
    choose = 383
    count = 383
elif 983 > count2 > 383 and 983 >= count1 >= 383:
    if count1<=count2:
        choose = 183
        count = count1
    else:
        choose = 383
        count = count2
elif count1 >= 983 and count2 >= 983 and count3 <= 983:
    choose = 983
    count = 983
elif count1 > 983 and count2 > 983 and count3 > 983:
    if count1<=count2 and count1<=count3:
        choose = 183
        count = count1
    elif count2<count1 and count2<=count3:
        choose = 383
        count = count2
    elif count3<count1 and count3<count2:
        choose = 983
        count = count3
print(choose)
print(round(count))
