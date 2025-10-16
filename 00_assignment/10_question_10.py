arr = [1,2,3,4,5,6,7,8,9,10]
i = 0 
j = 1 

while(1) : 
    temp = arr[j] 
    arr[j] = arr[i] 
    arr[i] = temp 
    i += 2 
    j += 2 
    if i == len(arr)-2 and j ==len(arr)-1 : 
            temp = arr[j] 
            arr[j] = arr[i] 
            arr[i] = temp 
            break 

print("The new array is :",arr)
