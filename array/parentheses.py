text = input()
check = []
for i in range(0,len(text)):
    check.append(text[i])
if (check.count('(') + check.count(')')) % 2 == 0:
    for i in range(0,check.count(')') - 1):
        check.remove(check[0])
        check.pop()
        while check[0] != '(':
            check.remove(check[0])
        while check[len(check)-1] != ')':
            check.pop()
    check.remove(check[0])
    check.pop()
    print(''.join(check))
    print(eval(''.join(check)))
else:
    print('ERROR INPUT')
#eval#
