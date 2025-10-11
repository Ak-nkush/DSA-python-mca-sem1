# print the pyramid in the palindrone pattern : 

num = int(input("Enter the value for num : ")) 
# 3 loops : 1st - spaces , 2nd loop - ascending order , 3rd loop - descending order 

for i in range (1,num+1) : 
    for j in range(i,num-i+1): 
        print(" ",end=" ")
    for j in range(1, i+1):
        print(j,end=" ") 
    for k in range()