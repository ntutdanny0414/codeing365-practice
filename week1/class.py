c = input()
h = int(input())
if h == 2:
    t1 = input()
    t2 = input()
    a1 = set()
    a1.add(t1)
    a1.add(t2)
else:
    t1 = input()
    t2 = '11'
    a1 = set()
    a1.add(t1)

c2 = input()
h2 = int(input())
if h2 == 2:
    t21 = input()
    t22 = input()
    a2 = set()
    a2.add(t21)
    a2.add(t22)
else:
    t21 = input()
    t22 = '11'
    a2 = set()
    a2.add(t21)
    
c3 = input()
h3 = int(input())
if h3 == 2:
    t31 = input()
    t32 = input()
    a3 = set()
    a3.add(t31)
    a3.add(t32)
else:
    t31 = input()
    t32 = '11'
    a3 = set()
    a3.add(t31)
    
if not len(c)==4 or not len(c2)==4 or not len(c3)==4:
    print('-1')
elif h>2 or h2>2 or h3>2:
    print('-1')
elif not 1 <= int(t1[0]) <=5 or not 1 <= int(t2[0]) <=5 or not 1 <= int(t21[0]) <=5 or not 1 <= int(t22[0]) <=5 or not 1 <= int(t31[0]) <=5 or not 1 <= int(t32[0]) <=5:
    print('-1')
elif not 1 <= int(t1[1]) <=8 or not 1 <= int(t2[1]) <=8 or not 1 <= int(t21[1]) <=8 or not 1 <= int(t22[1]) <=8 or not 1 <= int(t31[1]) <=8 or not 1 <= int(t32[1]) <=8:
    print('-1')
else:
    k1 = a1&a2
    k = 0
    if len(k1) == 1:
        print(c+','+c2+','+k1.pop())
        k = 1
    elif len(k1) == 2:
        print(c+','+c2+','+t1)
        print(c+','+c2+','+t2)
        k = 2
    k2 = a1&a3
    if len(k2) == 1:
        print(c+','+c3+','+k2.pop())
        k = 1
    elif len(k2) == 2:
        print(c+','+c3+','+t1)
        print(c+','+c3+','+t2)
        k = 2
    k3 = a2&a3
    if len(k3) == 1:
        print(c2+','+c3+','+k3.pop())
        k = 1
    elif len(k3) == 2:
        print(c2+','+c3+','+t21)
        print(c2+','+c3+','+t22)
        k = 2
    if k ==0:
        print('correct')
    
