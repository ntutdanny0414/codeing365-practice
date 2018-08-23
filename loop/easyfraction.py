from fractions import Fraction##
def print_fraction(z):
    if z > 1 and z.denominator != 1:#int#
        z1 = z - int(z)
        print(str(int(z))+'('+str(z1)+')')
    elif z < -1 and z.denominator != 1:
        z1 = z - int(z)
        print(str(int(z))+'('+str(abs(z1))+')')
    else:
        print(z)

one = [int(i) for i in input().split('/')]
two = [int(i) for i in input().split('/')]

if len(one) == 1:
    one.append(1)
if len(two) == 1:
    two.append(1)
if one[0] == 0 or one[1] == 0 or two[0] == 0 or two[1] == 0:
    print('ERROR')
    print('ERROR')
else:
    x = Fraction(one[0],one[1])
    y = Fraction(two[0],two[1])
    print_fraction(x+y)
    print_fraction(x*y)

