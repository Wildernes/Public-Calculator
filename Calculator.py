num1 = int(input('Enter your 1st Integer: '))
num2 = int(input('Enter your 2nd Integer: '))
op = 'Enter your operator: [+,-,*,/,%]'
if op == '+':
    result = num1+num2
elif op == '-':
    result = num1-num2
elif op == '*':
    result = num1*num2
elif op == '/':
    result = num1/num2
elif op == '%':
    result = num1%num2
else:
    print('Wrong Operator. Try Again :)')
print(num1, op, num2, '=', result)