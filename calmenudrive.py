print("1. Addition\n2. Substraction\n3. Multiplcation\n4. Division\n")
choice=int(input("Enter your choice : "))
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
if(choice==1):
    print(a+b)
elif(choice==2):
    print(a-b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    if(b==0):
        print("Invalid")
    else:
        print(a/b)
else:
    print("Invalid")
