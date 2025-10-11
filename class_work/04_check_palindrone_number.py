# Q. Check whether the number is palindrone or not 

def check_palindrone(num) :
    n = num  
    new_num = 0  
    while n>0 : 
        new_num = (new_num*10) + (n%10) 
        n = n // 10 
    if new_num == num : 
        print("It's a palindrone ") 
    else : 
        print("not a palindrone ")

num = int(input("Enter the number : ")) ; 
check_palindrone(num) 
