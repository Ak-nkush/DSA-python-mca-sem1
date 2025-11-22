class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.data
        self.top = self.top.next
        return val
    
    def is_empty(self):
        return self.top is None


class Queue: 
    def __init__(self):
        self.front = None 
        self.rear = None 
    
    # Enqueue an element into the queue.
    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    # displaying the elements of the queue 
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Dequeue an element from the queue.
    def dequeue(self):
        if self.front is None:
            return None
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val
    
    
    
    # Peek the front element of the queue.
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    # Reverse the queue using stack.
    def reverse(self):
        s = Stack()

        while self.front is not None:
            s.push(self.dequeue())

        while not s.is_empty():
            self.enqueue(s.pop())



q = Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.enqueue(55)

print("\nQueue after enqueues(insertion):")
q.display()

removed = q.dequeue()
print("\nDequeued element:", removed)

print("Queue after dequeue(Deletion):")
q.display()

print("\nPeek element:", q.peek())

print("\nBefore reversal:")
q.display()

q.reverse()
print("After reversal:")
q.display()


