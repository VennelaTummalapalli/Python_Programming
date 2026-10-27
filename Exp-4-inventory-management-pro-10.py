inventory={"Laptop":25,"Mouse":80,"Keyboard":50}
item=input("Enter Item:")
for item in inventory:
    print("Stock=",inventory[item])
else:
    print("Item Not Available")
