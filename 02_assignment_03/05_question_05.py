def tower_of_hanoi(n,A,B,C) : 
    if n==1 : 
        print("Move disk from the source ", A , " to destination " , C ) 
        return 
    tower_of_hanoi(n-1,A,C,B) 
    tower_of_hanoi(1,A,B,C) 
    tower_of_hanoi(n-1,B,A,C)  

n = 3
tower_of_hanoi(n,'A','B','C') 