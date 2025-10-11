# Write a program to count and print the number of vowels, consonants, digits, words, lines, special characters in a given text.
# string = input("Enter the string : ")
# vowels = 0 -> a ,e , i , o , u 
# consonants = 0 -> else part of vowels 
# digit -> 1 to 9 
# special_char -> further else part of vowels 
# words  -> words can be determines by numbers spaces in a sentence = spaces + 1 = number of words 
# lines -> here we can use special character \n 
# input -> it should be of multiply lines -> it has to be implement using while loop 




# vowels = 0 
# consonants = 0
# digits = 0 
# special_char = 0 
# lines = 0 
# for i in final_string : 
#     alpha_check = False
#     digit_check = False  
#     if(i=='a' or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U") : 
#         vowel_check = True  
#         vowels += 1 
#     elif(i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
#         digit_check = True 
#         digits += 1 
#     elif(alpha_check == True or digit_check == True){
#         # if its vowel or a digit it can't be consonants 
#     }

# actual code starts from here :-> ASCII table appreaoch : o(N^2) complexity 

flag = 1 
final_string = ""
while(flag) : 
    str = input("Enter the string: ")
    flag = int(input(("If you want to enter new line press 1 else press 0 : "))) 
    final_string = final_string + str + "\n" 

vowels = 0 
consonants = 0 
lines = 0 
digits = 0 
special_chars = 0 

for i in final_string : 
    ascii_value_i = ord(i) 
    for j in range(97,122+1) : 
        if 
        if(i=="a" or i=="e" or  i=="i" or i=="o" or i=="u") : 
            vowels += 1 
        else : 
            consonants += 1 
    for k in range(65,90+1) : 
        if ascii_value_i == k : 
            consonants += 1 
    for l in range(48,57+1): 
        if ascii_value_i == l : 
            digits += 1 
    if(i == 10) : 
        lines += 1
        continue
    else : 
        special_chars += 1 

print(vowels)
print(consonants)
print(digits)
print(lines)
print(special_char)


    
    



