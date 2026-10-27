s1=input("Enter First String:")
s2=input("Enter Second String:")
if sorted(s1.lower())==sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")
