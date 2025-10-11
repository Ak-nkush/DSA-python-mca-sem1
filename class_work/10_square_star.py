num = int(input("Enter the number of rows for number pattern : "))
spaces = 1 
for i in range(1,num+1) :
    for j in range (1,num+1) : 
      if(i == 1 or i == 5 or j==1 or j==5) : 
        print("*" , end=" ")
    else : 
        print("" ,end = " ")
    
    print()  