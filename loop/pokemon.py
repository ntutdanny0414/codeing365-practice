def is_float(s):#check#
    try:
        float(s)
        return True
    except ValueError:
        return False

def checknum1(n):
    if is_float(n) and -100 < float(n) < 0 and n.count('.')==1 and len(n.split('.')[1]) == 1 and len(n.split('.')[0]) >= 2:
        return True
    else:
        return False

def checknum2(c):
    if is_float(c) and 0 < float(c) < 30000 and c.count('.')==1 and len(c.split('.')[1]) == 1 and len(c.split('.')[0]) >= 1:
        return True
    else:
        return False

def checknum3(w):
    if w.isdigit() and 0 < int(w) < 10000:
        return True
    else:
        return False
    
n,c,w = input().split()

if not checknum1(n) or not checknum2(c) or not checknum3(w):
    print('Error')
else:
    need = float(n)
    player = float(c)
    number = int(w)
    success = 0
    while number != 0:
        if player + need >= 0:
            success = success + 1
            number = number - 1
            player = player + need + 1.5
        else:#???#
            number = number - 1
            player = player + 1.5
    print(success)
