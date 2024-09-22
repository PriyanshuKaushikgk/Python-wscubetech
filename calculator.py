num1 = int(input('enter the value1:-'))
num2 = int(input('enter the value2:-'))
operator = input("Enter the operator:-")
if(operator == '+'):
    print(num1+num2)
elif(operator == '-'):
    print(num1-num2)
elif(operator=='*'):
    print(num1*num2)
elif(operator=='/'):
    print(num1/num2)
else:
    print("Input mismatch")