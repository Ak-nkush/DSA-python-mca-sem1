arr = [12,23,45,67,88,99]
key = 45 
search = False 
# here we can't use for i in range , because range() function requires integers as a parameter , upper limit and lower limit 

for i in arr : 
    if  i == key : 
        search = True 
        break 

if (search) : 
    print("Key is found") 
else : 
    print("Key is not found")

# Q : determine the location of the key 