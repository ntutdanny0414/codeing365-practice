import math
a = int(input())
b = int(input())
c = int(input())
t = b*b-4*a*c
t2 = 4*a*c-b*b
if t >= 0:
    t1 = math.sqrt(t)
    print(int(((-b+t1)/(2*a))*10)/10)
    print(int(((-b-t1)/(2*a))*10)/10)
elif t<0:
    t1 = math.sqrt(t2)
    if t1/(2*a)<0:
        print(str(int(((-b)/(2*a))*10)/10)+'-'+str(abs(int((t1/(2*a))*10)/10))+'i')    
        print(str(int(((-b)/(2*a))*10)/10)+'+'+str(abs(int((t1/(2*a))*10)/10))+'i')
    else:
        print(str(int(((-b)/(2*a))*10)/10)+'+'+str(int((t1/(2*a))*10)/10)+'i')    
        print(str(int(((-b)/(2*a))*10)/10)+'-'+str(int((t1/(2*a))*10)/10)+'i')
#    print(str('{:.1f}'.format((-b)/(2*a)))+'+'+str('{:.1f}'.format(t1/(2*a)))+'i')
#    print(str('{:.1f}'.format((-b)/(2*a)))+'+'+str('{:.1f}'.format(t1/(2*a)))+'i')
#math.floor((t1/(2*a))*10)/10
#math.floor(((-b)/(2*a))*10)/10
#math.floor(((-b+t1)/(2*a))*10)/10
#math.floor(((-b-t1)/(2*a))*10)/10
