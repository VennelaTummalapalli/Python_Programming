print("1.add\n2.sub\n3.mul\n4.div\n5.exist\n")
ch = int(input("Enter your choice: "))
while ch <= 5:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    elif ch==5:
        print("exist")
    else:
        print("Invalid")
ch=int(input("enter your choice"))
