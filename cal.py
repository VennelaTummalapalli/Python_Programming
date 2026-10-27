num1 = int(input("enter a number: "))
num2 = int(input("enter b number: "))
op = input("please enter a operator{+,-,*,/,//,%}: ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "//":
    print(num1//num2)
elif op == "%":
    print(num1%num2)
else:
    print("invalid operator")

