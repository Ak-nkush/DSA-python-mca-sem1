def binary_search(arr,low,high,key):
    mid = (low+high)//2 
    if (key == arr[mid]) : 
        flag = True 
        return True 
    elif(key>arr[mid]) : 
        low = mid + 1 
        binary_search(arr,low,high,key)
    elif(key<arr[mid]) : 
        high = mid -1
        binary_search(arr,low,high,key)

arr = [5,7,8,10,20,23,43,55]
low = 0 
high = len(arr)- 1 
mid = (low+high)//2 
key = 43

check = binary_search(arr,low,high,key) 
if check : 
    print("Key is found")
    # print(f"Where key is present at {mid} index ")
else : 
    print("Key is not found")


