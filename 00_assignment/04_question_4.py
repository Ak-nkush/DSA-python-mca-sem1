str = input("Enter the sentence : ")
sub_string = input("Enter the word to be find : ")

index = 0 
subString_position = []
while(1):
    check_index = str.find(sub_string,index)
    if check_index != -1 : 
        subString_position.append(check_index)
        index = check_index + 1 
    else : 
        break 

print("The position of the Substring in a given String are ",end="")   
print(subString_position) 
for i in subString_position : 
    print(i,end=" ")



