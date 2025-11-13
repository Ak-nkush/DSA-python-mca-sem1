class Node : 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 
    
class LinkedList : 
    def __init__(self) : 
        self.head = None 
    
    #insertion at the end -> append 
    def append(self,data) : 
        new_node = Node(data)   
        if(self.head == None) : 
            self.head = new_node
        else : 
            temp = self.head
            while temp.next : 
                temp = temp.next 
            temp.next = new_node 
    
    # print the list 
    def print(self) : 
        temp = self.head
        while temp : 
            print(temp.data,end="->")
            temp = temp.next 
        print("None")
    
    #insert the node at sepecific position 
    def insert_at_position(self,position,data):
        if position <= 0 : 
            print("Enter the valid position ")
            return 
        else : 
            new_node = Node(data)
            temp = self.head 
            current_position = 1 

            if position == 1 : 
                new_node.next = self.head
                self.head = new_node 
                return 

            while temp and current_position < position - 1 : 
                temp = temp.next 
                current_position += 1 
            
            before_position = temp 
            after_position = temp.next 
            before_position.next = new_node
            new_node.next = after_position 
        
    #delete the last node : 
    def delete_last(self) : 
            node_A = self.head 
            node_B = node_A.next 
            
            while node_B.next : 
                node_A = node_A.next 
                node_B = node_B.next 
            
            node_A.next = None 
        
    # Search for an element in the list.
    def search_element(self,key) : 
            temp = self.head 
            status = False 
            while temp  :
                if temp.data == key : 
                    status = True 
                temp = temp.next 
            if status : 
                print("Element is present in the linked list ")
            else : 
                print("Element is not present in the linked list ")
        
    # Search for an element in the list
    def min_max(self) : 
            mini = self.head.data
            maxi = self.head.data
            temp = self.head 

            while temp : 
                mini = min(mini,temp.data)
                maxi = max(maxi,temp.data)
                temp = temp.next 
            
            return mini,maxi 
        
    #	Count Even and odd value nodes.	(Easy)
    def count_even_odd(self) : 
            even_count = 0 
            odd_count = 0 
            temp = self.head 
            while temp : 
                if temp.data % 2 == 0 : 
                    even_count += 1 
                else : 
                    odd_count += 1 
                temp = temp.next 
            return even_count,odd_count 

    # merging two list 
    def merge_list(self,l2) : 
            temp = self.head 
            while temp.next : 
                temp = temp.next 
            temp.next = l2.head 
            l2.head = None 
        
    # reversing the linked list 
    def reverse_linkedList(self) : 
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next

        
        arr.reverse()

        temp = self.head
        i = 0
        while temp:
            temp.data = arr[i]
            i += 1
            temp = temp.next




l1 = LinkedList()


l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
print("After appending nodes:")
l1.print()  


l1.insert_at_position(3, 25)
print("After inserting 25 at position 3:")
l1.print()   


l1.delete_last()
print("After deleting the last node:")
l1.print()   


print("Searching for element 25:")
l1.search_element(25)  
print("Searching for element 99:")
l1.search_element(99)  

mini, maxi = l1.min_max()
print(f"Minimum value: {mini}, Maximum value: {maxi}")


even, odd = l1.count_even_odd()
print(f"Even nodes: {even}, Odd nodes: {odd}")


l2 = LinkedList()
l2.append(50)
l2.append(60)
print("Second list:")
l2.print()

l1.merge_list(l2)
print("After merging list2 into list1:")
l1.print()

l1.reverse_linkedList()
print("After reversing the list:")
l1.print()

        





                
        
            

            


