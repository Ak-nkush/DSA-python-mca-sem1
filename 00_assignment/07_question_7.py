# Q: Replacing all the occurrence of the substring with another substring 
str = input("Enter the string : ") 
key = input("Enter the word which you want to replace: ")
newWord = input("Enter the new word: ")

if str.find(key) != -1 : 
    # it means word exists 
    str = str.replace(key,newWord) 
    print("New sentence is: ")
    print(str)
else  : 
    print("The word is not found")