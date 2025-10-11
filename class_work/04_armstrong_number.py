# Q. check whether the number is armstrong number 
# logic : sum of cube of a digit = a number 
# ex : 153  = 1cube + 3cube + 5cube = 153 


def Check_armstrong(num) : 
    sum = 0 
    while(num>0) : 
        sum = sum + ((num%10)**3) 
        num = num//10  
        #  in python // (double slash) is use to get a integer part of the quotion 
    return sum 

num = int(input("Enter the number : ")) ; 
ans = Check_armstrong(num) 
print(ans)
if(num == ans ) : 
    print("Got armstrong Number ")
else : 
    print("No armstrong NUmber ")