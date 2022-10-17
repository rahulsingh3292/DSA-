
class Solution:
  def isUnivalTree(self,root):
      if root.left is None and root.right is None: 
        return True 
      Q = [] 
      Q.append(root) 
      while Q:
        temp = Q.pop(0) 
        if temp.left:
          Q.append(temp.left) 
        if temp.right:
          Q.append(temp.right) 
        
        if Q and  temp.val != Q[0].val: 
          return False 
      return True 
  
  def isUnivalTree(self,root):
    main = root.val 
    def dfs(self,root):
      if root is None: return True 
      if root.val != main: 
        return False  
      return dfs(root.left) and dfs(root.right)
    return dfs(root)
       
      
    
    
    
    
    