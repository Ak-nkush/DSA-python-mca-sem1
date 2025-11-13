str = input("Enter the string : ") 

start = 0 
end = 0 
longest = "" 


for i in range(0,len(str)): 
    if str[i] == " " or i==len(str)-1  : 
        if i == len(str)-1 : 
            end = len(str)
        else :
             end = i
        word = str[start:end] 

        if len(longest)<len(word) : 
            longest = word
        start = end + 1 

print("The longest word in the given string is",longest)