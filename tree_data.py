
class Node:
  def __init__(self,val=None):
    self.val = val
    self.left = None 
    self.right=None 

root = Node(3) 
root.left = Node(5) 
root.right = Node(1) 
root.left.left= Node(6) 
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right= Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
"""
rootY = Node(1)
rootY.left = Node(2)
rootY.right= Node(2)
rootY.left.left= Node(3)
rootY.left.right= Node(4)
rootY.right.left= Node(4)
rootY.right.right= Node(3)
"""
"""
rootY = Node(1)
rootY.left = Node(2)
rootY.right= Node(2)
rootY.right.right= Node(3)
rootY.left.right= Node(3)
"""





"""
             3
          /    \
         5       1 
       /   \   /   \
      6     2  0    8 
          /  \ 
         7    4
"""
 

