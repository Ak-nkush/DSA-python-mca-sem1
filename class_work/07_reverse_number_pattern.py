num = int(input("Enter the number of rows for number pattern : "))

for i in range(1,num+1) : 
    for j in range (num,i-1,-1) : 
        #  declaration in the range function - first start point , second end pt . third flow(incr/decr)
        print(j, end=" ")
    print()  