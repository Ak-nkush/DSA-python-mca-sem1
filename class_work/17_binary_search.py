arr = [5,7,8,10,20,23,43,55]
low = 0 
high = len(arr)- 1 
mid = (low+high)//2 
flag = False 
key = 43

while(low<=high) : 
    if (key == arr[mid]) : 
        flag = True 
        break

    elif(key>arr[mid]) : 
        low = mid + 1 
    elif(key<arr[mid]) : 
        high = mid -1 

    mid = (low+high)//2 

if flag : 
    print("Key is found")
    print(f"Where key is present at {mid} index ")
else : 
    print("Key is not found")
