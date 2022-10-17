
from tree_data import *

class Solution:
  def __init__(self):
    self.total = 0 
    
  def get(self,root,curr):
    if root is None:
      return 

    curr = (curr*10)+root.val
    if root.left is None and root.right is None:
      self.total +=curr 

    self.get(root.left,curr)
    self.get(root.right,curr)
    curr=curr//10
    
  def sumNumbers(self,root):
    self.get(root,0)
    return self.total
  
  
 

print(Solution().sumNumbers(root))