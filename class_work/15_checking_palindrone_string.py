st = input("Input the string : ")

i = 0 ; 
j = len(st) - 1 

check = True
while(i<=j) : 
    if(st[i]!=st[j]) :
         check = False 
         break 
    i = i+1 
    j = j-1

if(check): 
    print("Given string is palindrone")
else : 
    print("Given string is not palindrone")

