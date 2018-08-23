x1 = int(input())
if x1 == 10:
    x2 = 0
else:
    x2 = int(input())
x3 = int(input())
if x3 == 10:
    x4 = 0#x5 = input()
else:
    x4 = int(input())
x5 = 0
if (x3 == 10 and x4 == 10) or (x3 == 10 ) :
    x5 = int(input())
count = 0
count = x1 + x2 + x3 + x4 + x5 
print(count)
