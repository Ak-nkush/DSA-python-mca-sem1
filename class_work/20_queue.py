class Node : 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 

class Queue : 
    def __init__(self) : 
        self.front = None 
        self.rear = None 
    
    def enqueue(self,data) : 
        new_node = Node(data)
        if self.rear == None and self.front == None : 
            self.rear = new_node 
            self.front = new_node 
        else : 
            self.rear.next = new_node
            self.rear = new_node 
    
    def display(self) : 
        temp = self.front 
        while temp : 
            print(temp.data , end = "->")
            temp = temp.next 
        print("None")
    
    def dequeue(self) : 
        front = self.front 
        self.front = front.next 
    
    def 
    

q1 = Queue() 
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.display() 
q1.dequeue() 
q1.display()

 

