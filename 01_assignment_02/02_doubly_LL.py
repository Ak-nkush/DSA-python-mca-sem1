class Node : 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 
        self.prev = None 

class Doubly_linkedList  :
    def __init__(self) : 
        self.head = None 
        self.tail = None 
    
    #append the node at the end of the list 
    def append(self,data) : 
        new_node = Node(data)
        if self.head == None and self.tail == None : 
            self.head = new_node
            self.tail = new_node 
            return 
        else : 
            self.tail.next = new_node 
            new_node.prev = self.tail
            self.tail = new_node 
    
    #insert the node at the beginning 
    def prepend(self,data) : 
        new_node = Node(data)
        if self.head == None and self.tail == None : 
            self.head = new_node
            self.tail = new_node 
            return 
        else : 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
    
    # display the dll 
    def display_from_front(self): 
        temp = self.head
        while temp : 
            print(temp.data,end="<->")
            temp = temp.next 
        print("None")
    
    # delete the node at the specfic position 
    def delete_at_position(self,position): 
        if position <= 0 : 
            print("Enter the valid position ")
            return 
        
        current_position = 1 
        temp = self.head 

        while temp and current_position < position:  
            current_position += 1
            temp = temp.next 
        
        if temp is None:
         print("Position out of range.")
         return
        
        if temp.prev is None:
         self.head = temp.next
         if self.head:
            self.head.prev = None
         return

    
        if temp.next is None:
         temp.prev.next = None
         return
            
        before = temp.prev 
        after = temp.next 
        before.next = after 
        after.prev = before
    
    # search for the element 
    def search_element(self,key)  :
        temp = self.head 
        flag = False
        while temp : 
            if temp.data == key : 
                flag = True
            temp = temp.next 
        if flag : 
            print("Element is present in doubly linked list")
        else : 
            print("Element is not present in doubly linked lisr")
    
    # count total number of nodes : 
    def count_nodes(self) : 
        temp = self.head 
        countofNodes = 0 
        while temp : 
            countofNodes += 1 
            temp = temp.next 
        return countofNodes
     
    # deleting the middle 
    def delete_middle(self):
    
     if self.head is None or self.head.next is None:
        self.head = None
        return

     temp = self.head
     count = 0
     while temp:
        count += 1
        temp = temp.next

     middle_pos = count // 2 + 1  
    
     temp = self.head
     current_position = 1
     while temp and current_position < middle_pos:
        temp = temp.next
        current_position += 1 

     before = temp.prev
     after = temp.next

     # If deleting the head (edge case)
     if before is None:
        self.head = after
        if after:
            after.prev = None
        return

     # If deleting the tail (edge case)
     if after is None:
        before.next = None
        return

     # Normal middle node deletion
     before.next = after
     after.prev = before
              

    # reverse the doubly linked list : 
    def reverse_doubly_linkedList(self) : 
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





dll = Doubly_linkedList()


dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
print("After appending nodes at the end:")
dll.display_from_front()   


dll.prepend(5)
print("After inserting 5 at the beginning:")
dll.display_from_front()  


dll.delete_at_position(3)
print("After deleting node at position 3:")
dll.display_from_front()   


print("Searching for element 30:")
dll.search_element(30)   
print("Searching for element 100:")
dll.search_element(100)  


count = dll.count_nodes()
print(f"Total nodes in the list: {count}")  

dll.delete_middle()
print("After deleting the middle node:")
dll.display_from_front()   

dll.reverse_doubly_linkedList()
print("After reversing the doubly linked list:")
dll.display_from_front()   
