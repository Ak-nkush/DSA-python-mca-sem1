num = int(input("Enter the number of rows for number pattern : "))

for i in range(1,num+1) : 
    for j in range (1,i+1) : 
        print(j, end=" ")
    print()  