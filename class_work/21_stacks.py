class Node:
    def __init__(self, data):
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
    
    # displaying the elements of the stacks 
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

s = Stack()

print("\nPushing the elements into stacks : ")
s1 = Stack() 
s1.push(11)
s1.push(22)
s1.push(33)
s1.push(44)
s1.push(55)
s1.display() 

print("\nPoping elements from stacks : ")
s1.pop() 
s1.pop() 
s1.display() 

print("\nGetting the peek element : ") 
print(s1.peek())

print("\nStack before reversal : ")
s1.display()
s1.reverse() 
print("Stack after reversal : ")
s1.display() 
