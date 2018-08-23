import math
num1 = int(input())
num2 = int(input())
print('Sum:'+str('{:.2f}'.format(num1+num2)))
print('Difference:'+str('{:.2f}'.format(abs(num1-num2))))
print('Product:'+str('{:.2f}'.format(round(num1*num2,2))))
print('Quotient:'+str('{:.2f}'.format(math.floor((num1/num2)*100)/100)))
