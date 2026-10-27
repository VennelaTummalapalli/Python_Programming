contacts={}
while True:
    print("\nContact Management System")
    print("1.Add Contact\n2.Search Contact\n3.Update Contact\n4.Delete Contact\n5.Display Contact\n6.Exit\n")
    choice=int(input("Enter Choice:"))
    if choice==1:
        name=input("Enter Name:")
        phone=(input("Enter Phone:"))
        contacts[name]=phone
        print("Contact Added Successfull")
    elif choice==2:
         name=input("Enter Name:")
         if name in contacts:
             print("Phone:",contacts[name])
         else:
             print("Contacts Not Found")
    elif choice==3:
         name=input("Enter Name:")
         if name in contacts:
             phone=input("Enter New Phone:")
             contacts[name]=phone
             print("Update Sucsessfully")
         else:
            print("Contact Not Found")
    elif choice==4:
         name=input("Enter Name:")
         if name in contacts:
             del contacts[name]
             print("Deleted Successfully")
         else:
              print("Contact Not Found")
    elif choice==5:
        print("\nCONTACT LIST")
        for name,phone in contacts.item():
            print(name,"\t",phone)
    elif choice==6:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
