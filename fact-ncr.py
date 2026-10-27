num=5
r=2
fact_num=1
fact_r=1
fact_nr=1
for i in range(1,num+1):
    fact_num*=i
for i in range(1,r+1):
    fact_r*=i
for i in range(1,num-r+1):
    fact_nr*=i
ncr=fact_num//(fact_r*fact_nr)
print("Ncr of", num, "and", r,"is",ncr)
