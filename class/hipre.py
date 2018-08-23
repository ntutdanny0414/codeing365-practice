class HPre:
    def __init__(self,digit = None,decpt = None,sign = None):
        self.digit = digit
        self.decpt = decpt
        self.sign = sign
    def tenpower(self):
        return len(self.digit)-self.decpt
    def pluszero(self,pre):
        if self.tenpower() <= pre.tenpower():
            for i in range(pre.tenpower() - self.tenpower()):
                self.digit = self.digit + '0'
        else:
            for i in range(self.tenpower() - pre.tenpower()):
                pre.digit = pre.digit + '0'
    def __add__(self,pre):
        outpre = HPre()
        self.pluszero(pre)
        predigit = str(int(self.digit)*self.sign + int(pre.digit)*pre.sign)
        if predigit[0] == '-':
            presign = -1
        else:
            presign = 1
        predecpt = max(self.decpt,pre.decpt)+(len(predigit.lstrip('-'))-max(len(self.digit),len(pre.digit)))
        outpre.digit = predigit.lstrip('-').rstrip('0')#strip#
        outpre.decpt = predecpt
        outpre.sign = presign
        return outpre
    def __sub__(self,pre):
        outpre = HPre()
        self.pluszero(pre)
        predigit = str(int(self.digit)*self.sign - int(pre.digit)*pre.sign)
        if predigit[0] == '-':
            presign = -1
        else:
            presign = 1
        predecpt = max(self.decpt,pre.decpt)+(len(predigit.lstrip('-'))-max(len(self.digit),len(pre.digit)))
        outpre.digit = predigit.lstrip('-').rstrip('0')#strip#
        outpre.decpt = predecpt
        outpre.sign = presign
        return outpre
    def __mul__(self,pre):
        outpre = HPre()
        self.pluszero(pre)
        predigit = str(int(self.digit)*self.sign * int(pre.digit)*pre.sign)
        if predigit[0] == '-':
            presign = -1
        else:
            presign = 1
        point1 = len(self.digit) - self.decpt
        point2 = len(pre.digit) - pre.decpt
        predecpt = len(predigit)-(point1+point2)
        outpre.digit = predigit.lstrip('-').rstrip('0')#strip#
        outpre.decpt = predecpt
        outpre.sign = presign
        return outpre
def check(string):
    check = string.lstrip('-')
    if len(check.split('.')[0]) > 1 and check[0] == '0':
        return False
    else:
        return True
def splitstring(num):
    check = num.lstrip('-')
    if num[0] == '-':
        sign = -1
    else:
        sign = 1    
    if float(check) < 1:
#        decpt = (check.count('0')-1)*(-1)#float < 0#
        muln = float(check)
        count = 0
        while muln < 0.1:
            count = count - 1
            muln = muln * 10
        decpt = count
    else:#.position#
#        decpt = check.index('.')
        decpt = len(check.split('.')[0])
    digit = num.lstrip('-').replace('.','').lstrip('0')#no remove#
    if len(digit) > 20:
        digit = digit[:20]
    return [digit,decpt,sign]
num1 = input()
num2 = input()
fun = input()
if check(num1) and check(num2):
    data1 = splitstring(num1)
    data2 = splitstring(num2)
    x = HPre(data1[0],data1[1],data1[2])
    y = HPre(data2[0],data2[1],data2[2])
    if fun == 'a':
        z = x + y
    elif fun == 's':
        z = x - y
    elif fun == 'm':
        z = x * y
    if len(z.digit) > 20:
        z.digit = z.digit[:20]
    print('digit='+z.digit)
    print('decpt='+str(z.decpt))
    print('sign='+str(z.sign))
else:
    print('input error')
        
        
        
    
