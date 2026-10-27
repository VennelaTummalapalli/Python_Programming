f=open("a.txt","r")
print(f.readline())
print(f.readline())
print(f.readlin())
f.close()

with open("a.txt","r") as f:
    print(f.read(3))
    print(f.readline())
    print(f.readlines())
