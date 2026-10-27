for i in range(5):
    print("1.Add\n2.Sub\n3.Multiply\n4.Division\n")
    a=int(input("1st number : "))
    b=int(input("2nd number : "))
    ch=int(input("enter choice : "))
    if(ch==1):
        print(a+b)
        print()
    elif(ch==2):
        print(a-b)
        print()
    elif(ch==3):
        print(a*b)
        print()
    elif(ch==4):
        if(b==0):
            print("invalid")
            print()
        else:
            print(a/b)
            print()
    elif(ch==5):
        break
