x1 = int(input())
x2 = int(input())
y1= int(input())
y2 = int(input())
z1= int(input())
z2 = int(input())
count = 0
count = (x2 - x1)+(y2 - y1)+(z2 - z1)
if x2>=y1>x1:
    count = count - (x2 - y1)
#elif y2>x1>=y1 and y2>=x2>y1:
#    count = count - (x2 - x1)
#elif x2>=y1>x1 and x2<=y2:
#    count = count - (x2 - y1)
#elif x2>y1>=x1 and x2>=y2>x1:
#    count = count - (y2 - y1)
if y2>=z1>x1:
    count = count - (y2 - z1)
print(count)
