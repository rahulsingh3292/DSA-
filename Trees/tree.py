
from tree_data import root 

class Tree:
  def levelOrderTraversal(self,root):
    queue = [] 
    queue.append(root)
    while queue:
      temp = queue.pop(0)
      print(temp.data,end=" ")
      
      if temp.left:
        queue.append(temp.left)
      
      if temp.right:
        queue.append(temp.right)
    print()
 
  def inOrder(self,root):
    if root is None: return 
    self.inOrder(root.left)
    print(root.data,end=" ")
    self.inOrder(root.right)
  
  def preOrder(self,root):
    if not root: return 
    print(root.data,end=" ")
    self.preOrder(root.left)
    self.preOrder(root.right)
    
  def postOrder(self,root):
    if root is None:
      return 
    self.postOrder(root.left)
    self.postOrder(root.right)
    print(root.data,end=" ")
    
tree = Tree()
#tree.inOrder(root)
print()
tree.preOrder(root)
print()
#tree.postOrder(root)

        
  
