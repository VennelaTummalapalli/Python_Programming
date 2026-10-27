roll_no="MCA101"
print(roll_no.isalnum())
print(roll_no.isdigit())

text=input("Enter age:")
if text.isdigit():
    age=int(text)
    print("valid number:",age)
else:
    print("Digits only,Please")
print(roll_no.split())
