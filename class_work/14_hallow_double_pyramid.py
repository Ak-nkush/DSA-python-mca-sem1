num = int(input("Enter the value for num : ")) 

for i in range(1,num+1) : 
    # first loop is for spaces 
    for j in range(1,num-i+1) : 
        print(" ",end=" ") 
    # second loop is for stars
    
    for k in range(1,(2(i)+1)) : 
        if(k==1 or k==(2(i)+1)) : 
            print("*",end=" ")
        else : 
            print("#",end=" ")
    print()
    