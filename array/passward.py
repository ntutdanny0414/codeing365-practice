import re

s = ''
while True:
    s = s+input()+' '
    if s[-2] == '.':
        break

pass1 = re.sub(r'\D', " ", s).split()#
passw = 0
for i in range(0,len(pass1)):
    if len(pass1[i]) >= 1:
        passw = passw +int(pass1[i][::-1])##
if len(str(passw)) > 4:
    passw = passw % 10000
elif len(str(passw)) == 3:
    passw = '0'+str(passw)
elif len(str(passw)) == 2:
    passw = '00'+str(passw)
elif len(str(passw)) == 1:
    passw = '000'+str(passw)
passw = str(passw)  
print(passw)
s2 = ''
while True:
    s2 = s2+input()+' '
    if s2[-2] == '.':
        break

fre = re.findall(r'[A-Za-z]',s2)##
for i in range(len(fre)):
    fre[i] = fre[i].lower()#to lower#
dic = {x:fre.count(x) for x in fre}##
dic = list(dic.items())##dic.items()
print(dic)
for i in range(0,len(dic)):
    if dic[i][1] >= 10:
        dic[i] = ' '
while ' ' in dic:##
    dic.remove(' ')##
def key(x):
    return x[1]
forthcount = sorted(dic ,key = key,reverse = True)##
for i in range(0,len(dic)):
    if dic[i][1] < forthcount[3][1]:
        dic[i] = ' '
while ' ' in dic:
    dic.remove(' ')
for i in range(len(dic)-1,-1,-1):
    if len(dic) == 4:
        break
    if dic[i][1] == forthcount[3][1]:
        dic[i] = ' '
while ' ' in dic:
    dic.remove(' ')
print(dic)
passw = passw+str(dic[0][1])+str(dic[1][1])+str(dic[2][1])+str(dic[3][1])
print(passw)
