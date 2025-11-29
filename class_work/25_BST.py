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
        
    def preorder(self,current=None): 
        current = self.root 
        if current is None  :        
            return 
        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)
        
        # postorder 



bst = BST()
for x in [50,30,70] : 
    bst.insert(x)
print("Inorder : ", end=" ") 
bst.inorder() 
bst.preorder()



