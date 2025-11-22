class Node : 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 

class LinkedList : 
    def __init__(self) : 
        self.head = None 
    
    def append(self,new_node) : 
        temp = self.head 
        #instead creating the newnode within it is passed as a parameter 

        if temp :  # if list is not empty 
            while temp.next : 
                temp = temp.next 
            temp.next = new_node
        else : 
            # if list is empty the node becomes the first node 
            self.head = new_node 
        
    def print_nodes(self) : 
        temp = self.head 
        while temp : 
            print(temp.data , end=" ") 
            temp = temp.next 
    
    # counting even and odd nodes 
    def count_even_odd(self) : 
        even = 0 
        odd = 0 
        temp = self.head 
        while temp : 
            if temp.data % 2 == 0 : 
                even+=1 
            else : 
                odd+=1 
            temp = temp.next 
        print("Even numbers nodes are : ",even) 
        print("odd numbers of nodes are ",odd)
    
    # key search 
    def search(self,key) : 
        temp = self.head 
        flag = 0 
        while temp : 
            if temp.data == key : 
               flag = 1 
               break 
            temp = temp.next 
        if flag : 
            print("Key is found")
        else : 
            print("Key is not found")
        
    #finding min and max nodes 
    def min_max(self):
        temp = self.head
        # note that first collect the value of the first node 
        mini = temp.data 
        maxi = temp.data 
        while temp : 
            maxi = max(maxi,temp.data)
            mini = min(mini,temp.data)
            temp = temp.next 
        print("maximum node is",maxi)
        print("minimum node is",mini)
    
    # joining two lists 
    def concat_lists(self,l2) : 
        temp = self.head 
        # why? -> while temp is not working -> because temp was pointing to the null 
        while temp.next: 
            temp = temp.next 
        temp.next = l2.head

    def NGE(self) : 
        temp_outside = self.head 
        while temp_outside : 
            temp_inside = temp_outside.next
           while temp_inside : 
              if temp_inside.data < temp_inside.next.data : 
                  print(f"({temp_outside.data},{temp_inside.next.data })") 
                  break 
            temp_inside = temp_inside.next 
        print(f"({temp_outside.data},{-1})") 
        temp_outside = temp_outside.next

    


    
    
list1 = LinkedList() 
list1.append((Node(1)))
list1.append((Node(2)))
list1.append((Node(3)))
list1.append((Node(4)))
list1.append((Node(5)))
list1.print_nodes() 
list1.NGE() 
