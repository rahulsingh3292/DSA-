from tree_data import root 

class Solution:
  def has(self,root,curr,target):
    if root is None:
      return False
    if root.left is None and root.right is None and curr+root.data == target:
      return True 
    return self.has(root.left,curr+root.data,target) or self.has(root.right,curr+root.data,target)
  
  
  def hasPathSum(self,root,target):
     return self.has(root,target)
  
    
target = 18
res = Solution().hasPathSum(root,target)
print(res)