n = int(input("Enter the value of n : "))

spaces = 1
for i in range(0,n) : 
    for s in range (spaces,n) : 
      print(" ",end="") 
    check = 2*i+1
    for j in range(0,check) : 
        if (j==0 or j==check-1):
           print("*",end="")
        else : 
            print(" ",end="")
    print()
    spaces = spaces + 1 

spaces = n-1 
lower = n-2 
for i in range(lower,-1,-1):
    for j in range(spaces,n) : 
        print(" ",end="")
    check2 = 2*i+1 
    for k in range(0,check2) : 
        if (k==0 or k==check2-1) : 
            print("*",end="")
        else : 
            print(" ",end="")
    print()
    spaces = spaces - 1 



