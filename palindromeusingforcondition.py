s=input("enter any string to copare").lower()
l=len(s)
for i in range(l//2):
    if(s[i]!=s[l-i-1]):
         print("not...")
print("palindrome")
   

