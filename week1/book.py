x = int(input())
y = int(input())
z = int(input())
count = 0
if 1<=x<=10:
    count = count + 380*x
elif 11<=x<=20:
    count = count + 380*x*0.9
elif 21<=x<=30:
    count = count + 380*x*0.85
elif x>=31:
    count = count + 380*x*0.8
if 1<=y<=10:
    count = count + 1200*y
elif 11<=y<=20:
    count = count + 1200*y*0.95
elif 21<=y<=30:
    count = count + 1200*y*0.85
elif y>=31:
    count = count + 1200*y*0.8
if 1<=z<=10:
    count = count + 180*z
elif 11<=z<=20:
    count = count + 180*z*0.85
elif 21<=z<=30:
    count = count + 180*z*0.8
elif z>=31:
    count = count + 180*z*0.7
print(round(count))
    
