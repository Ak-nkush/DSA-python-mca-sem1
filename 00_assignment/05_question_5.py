flag = 1 
final_string = ""
while(flag) : 
    str = input("Enter the string: ")
    flag = int(input(("If you want to enter new line press 1 else press 0 : "))) 
    final_string = final_string + str + "\n" 


final_string = final_string.lower() 
vowels = 0 
consonants = 0
digits = 0 
special_chars = 0 
lines = 0 
for i in final_string : 
    if (i>="a" and i<="z") : 
        if(i=='a' or i=="e" or i=="i"or i=="o" or i=="u") : 
            vowels += 1 
        else : 
            consonants += 1 
    elif(i>="0" and i<="9") : 
          digits += 1 
    elif(i == "\n") : 
         lines += 1 
    elif i != " ":
     special_chars += 1

   
print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")
print(f"Lines : {lines}")
print(f"Digits : {digits}")
print(f"Special Characters : {special_chars}")
    



    
    



