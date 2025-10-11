# Q. Calculating the factorial of the a number 
def fact(num) : 
    factorial = 1 
    for i in range(2,num+1) : 
        factorial = factorial * i 
    return factorial 

num = int(input("Enter the number : ")) ; 
ans = fact(num) 
print(f"factorial of a given number is {ans}")

