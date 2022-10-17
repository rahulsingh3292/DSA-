from collections import deque
from tree_data import * 
class Solution:
  def averageOfLevels(self,root):
    if root is None: return []
    if root.left is None and root.right is None:
      return [1/1] 
    
    Q = [root,None] 
    res = [] 
    avg=total= 0
 
    while len(Q)>1: 
      curr = Q.pop(0) 
      if curr == None:
        Q.append(None) 
      else:
        if curr.left:
          Q.append(curr.left)
        if curr.right:
          Q.append(curr.right) 
      if curr!=None:
        avg +=root.val 
        total +=1
      else:
        res.append(avg/total)
        
        avg=total = 0 
    res.append(avg/total)
    return res
 
print(Solution().averageOfLevels(root))