num = int(input("Enter the number of rows for number pattern : "))
spaces = 1 
for i in range(1,num+1) :
    
    for s in range(spaces ,num-i)  : 
        print(end=" ")
    for j in range (1,i+1) : 
        print(" * ", end=" ")
    spaces = spaces + 1 
    print()  