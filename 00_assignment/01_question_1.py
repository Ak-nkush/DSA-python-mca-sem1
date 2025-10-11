n = int(input("Enter the value of n : "))

spaces = 1 
num = n - 1
check = n   
count2 = 0 
for i in range(1,n+1) : 
    for s in range (spaces,n) : 
        print(" ",end=" ") 
    count1 = 1 
    for j in range (num,n) : 
        print(count1,end=" ")
        count1 = count1 + 1 
    count3 = count2
    for k in range(check,n) : 
        print(count3,end=" ")
        count3 = count3 - 1 
    
    print()
    spaces = spaces + 1 
    num = num - 1 
    count2 = count2 + 1 
    check = check - 1 
    