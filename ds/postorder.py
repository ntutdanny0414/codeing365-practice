eq = input()
stack = []
oper = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':4}#'('stop#
outcome = []
for i in eq:
    if i == '(':
        stack.append(i)
    elif i in oper:
        if len(stack) == 0:
            stack.append(i)
        elif oper[stack[len(stack)-1]] >= oper[i]:
            while oper[stack[len(stack)-1]] >= oper[i]:
                if stack[len(stack)-1] == '(':
                    break
                else:
                    outcome.append(stack.pop())
                if len(stack) == 0:#last#
                    break
            stack.append(i)
        else:
            stack.append(i)
    elif i == ')':
        while stack[len(stack)-1] != '(':
            outcome.append(stack.pop())
        stack.pop()#(#
    else:
        outcome.append(i)
while len(stack) != 0:#instack#
    outcome.append(stack.pop())
print(''.join(outcome))
        
         
        
            
    
