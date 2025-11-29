class Node: 
    def __init__(self,data): 
        self.data = data 
        self.right = None
        self.left = None 
    
class BST : 
    def __init__(self): 
        self.root = None 
    
    def insert(self,key): 
        newNode = Node(key)
        if self.root is None : 
            self.root = newNode 
            return 
        current = self.root 
        prev = None 
        while(current): 
            previous = current 
            if key < current.data : 
                current = current.left 
            else : 
                current = current.right 
        if key < previous.data : 
            previous.left = newNode 
        else : 
            previous.right = newNode 
    
    def inorder(self):
      stack = []
      current = self.root

      while True:
        while current:
            stack.append(current)
            current = current.left

        if not stack:
             break

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right
        
    def preorder_iterative(self):
      if self.root is None:
        return

      stack = [self.root]

      while stack:
         node = stack.pop()
         print(node.data, end=" ")

         if node.right:
            stack.append(node.right)
         if node.left:
            stack.append(node.left)
            
    def postorder_iterative(self):
     if self.root is None:
        return

     stack1 = [self.root]
     stack2 = []

     while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

     while stack2:
        print(stack2.pop().data, end=" ")
 


bst = BST()
for x in [50, 30, 70]:
    bst.insert(x)

print("Inorder: ", end="")
bst.inorder()

print("\nPreorder (iterative): ", end="")
bst.preorder_iterative()

print("\nPostorder (iterative): ", end="")
bst.postorder_iterative()




