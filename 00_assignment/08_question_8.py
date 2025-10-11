# Q: Write the program to check string contains onlu unique character is present or not 

str = input("Enter the string: ")
setof_characters = set()

for i in str : 
    setof_characters.add(i) 

if len(setof_characters) == len(str) : 
    print("string is unique")
else : 
    print("String is not unique")


