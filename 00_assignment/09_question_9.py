arr = [1,2,3,4,5,6,7,2,3,4,1]
unique_set = set() 

for i in arr :
    unique_set.add(i)

unique_arr = list(unique_set) 
print("The unique array is :" ,unique_arr)