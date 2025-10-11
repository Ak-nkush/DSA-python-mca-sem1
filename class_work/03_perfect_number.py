# Q. Check whether the number is perfect number or not 
#  a perfect number = sum of a divisor a number 
# series of a perfect number = 6,28,496,8128 

def perfectNumber(num) : 
    ans = 0 
    for i in range(1,num) :  
     if num%i == 0 : 
         ans = ans + i 
    return ans 

num = int(input("Enter the number : ")) ; 
ans = perfectNumber(num) 
if(num == ans ) : 
    print("Got perfect Number ")
else : 
    print("No perfect NUmber ")