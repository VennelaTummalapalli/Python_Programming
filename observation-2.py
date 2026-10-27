n = int(input("Enter a number: "))
fact_for = 1
for i in range(1, n + 1):
    if i == 2:
        pass 
    if i == 3:
        continue 
    if i > n:
        break  
    fact_for *= i
else:
    print("For loop completed successfully")
print("Factorial using for loop:", fact_for)

fact_while = 1
i = 1
while i <= n:
    if i == 2:
        pass  
    if i == 3:
        i += 1
        continue  
    if i > n:
        break
    fact_while *= i
    i += 1
else:
    print("While loop completed successfully")
print("Factorial using while loop:", fact_while)
