def factorial(num) : 
    for i in range(1,num+1):
        if num == 1 : 
            return 1 
        else : 
            return num*factorial(num-1) 


num = int(input("Enter the number : ")) ; 
ans = factorial(num) 
print(f"factorial of a given number is {ans}")