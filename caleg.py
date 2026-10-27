num1 = int(input("enter a number: "))
num2 = int(input("enter b number: "))
op=input("please enter a operator: 1.add\n 2.sub\n3.mul\n4.div\n")
if op == "add":
    print(num1 + num2)
elif op == "sub":
    print(num1 - num2)
elif op == "mul":
    print(num1*num2)
elif op == "div":
    print(num1/num2)
else:
    print("invalid operator")


