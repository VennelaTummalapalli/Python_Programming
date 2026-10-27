#maxtrix addition
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
C=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print(C)
for i in C:
    for j in i:
        print(j, end=" ")
    print()  
