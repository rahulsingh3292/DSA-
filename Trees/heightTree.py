

class Solution:
  def __init__(self):
    self._height = 0 
    
  def height(self,root,count=0):
    if root is None:
      self._height = max(self._height,count)
      return 
    self.height(root.left,count+1)
    self.height(root.right,count+1)
    count -=1
  
  def maxDepth(self,root):
    self.height(root)
    return self._height
