
class Node : 
    def __init__(self,data) : 
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None
    
    # Push an element onto the stack. 
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    # Pop an element from the stack.	
    def pop(self) : 
        if self.top is None:
            print("Stack Underflow")
            return None

        self.top = self.top.next 
    
    # Peek the top element of the stack.	
    def peek(self) : 
        return self.top.data
    
    # Reverse the stack
    def reverse(self):
        prev = None
        current = self.top

        while current:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
        
        self.top = prev

class Queue : 
    def __init__(self) : 
        self.front = None 
        self.rear = None 

    # Enqueue an element into the queue.
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
    

    # Dequeue an element from the queue.
    def dequeue(self) : 
        front = self.front 
        self.front = front.next 
    
    # peek the front of the element
    def getfront() : 
        if self.front == None : 
            print("Queue is empty ") 
            return 
        return self.front.data
    
    
    # reverse the queue using stacks : 
    def reverse(self) :
        stack = []

        while self.front is not None:
            stack.append(self.dequeue())

        while stack:
            self.enqueue(stack.pop())



 

