def vsearch(aorb,data):#big small#
    if aorb == 'a':
        return 'A'+':'+str(data)
    elif aorb == 'b':
        return 'B'+':'+str(data)
def wdraw(aorb,money):
    if aorb == 'a':
        return 'A'+':Withdraw,'+str(money)
    elif aorb == 'b':
        return 'B'+':Withdraw,'+str(money)
def ssave(aorb,money):
    if aorb == 'a':
        return 'A'+':Deposit,'+str(money)
    elif aorb == 'b':
        return 'B'+':Deposit,'+str(money)
def ppercent(adata,bdata):
    if adata <= 0 and bdata > 0:
        return 'A:0%,B:100%'
    elif adata > 0 and bdata <= 0:
        return 'A:100%,B:0%'
    elif adata == 0 and bdata == 0:
        return 'A:50%,B:50%'
    else:
        aper = int((adata / (adata+bdata)) * 100)
        bper = 100 - aper
        return 'A:'+str(aper)+'%,B:'+str(bper)+'%'

def start(aorb,data,compare,outcome):
    if aorb == 'a':
        outcome.append('Select A')
        while True:
            function = input()
            if function == 'v':
                outcome.append(vsearch(aorb,data))
            elif function == 'w':
                money = int(input())
                data = data - money
                outcome.append(wdraw(aorb,data))
            elif function == 's':
                money = int(input())
                data = data + money
                outcome.append(ssave(aorb,data))
            elif function == 'p':
                outcome.append(ppercent(data,compare))
            elif function == 'a':
                start('a',data,compare,outcome)
                break
            elif function == 'b':
                start('b',compare,data,outcome)
                break
            elif function == 'e':
                break
    elif aorb == 'b':
        outcome.append('Select B')
        while True:
            function = input()
            if function == 'v':
                outcome.append(vsearch(aorb,data))
            elif function == 'w':
                money = int(input())
                data = data - money#dataneedchange#
                outcome.append(wdraw(aorb,data))
            elif function == 's':
                money = int(input())
                data = data + money#+++#
                outcome.append(ssave(aorb,data))
            elif function == 'p':
                outcome.append(ppercent(compare,data))#now a is compare#
            elif function == 'a':
                start('a',compare,data,outcome)
                break
            elif function == 'b':
                start('b',data,compare,outcome)
                break
            elif function == 'e':
                break
aorb = input()
a = 0
b = 0
outcome = []
if aorb == 'a':
    start(aorb,a,b,outcome)
elif aorb == 'b':
    start(aorb,b,a,outcome)
for i in range(0,len(outcome)):
    print(outcome[i])
    
        
