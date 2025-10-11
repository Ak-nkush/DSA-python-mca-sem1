num = int(input("Enter the number of rows for number pattern : "))
spaces = 1 
for i in range(1,num+1) :
    #  spaces - 0 , 1 , 2 , 3 , 4 
    for s in range(spaces,0,-1) : 
        # here spaces are increasing soo we are using reverse for loop 
        print(end=" ")
    for j in range (num,i-1,-1) : 
        print("*" , end=" ")
    spaces = spaces + 1 
    print()  