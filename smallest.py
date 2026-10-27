a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))

if a<b and a<c:
    print("Smallest =",a)
elif b<c:
    print("Smallest =",b)
else:
    print("Smallest =",c)
