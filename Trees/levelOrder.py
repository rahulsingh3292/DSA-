
from tree_data import * 
class Solution:
  def levelOrder(self,root):
    if root is None: return []
    if root.left is None and root.right is None:
      return [1/1] 
    
    Q = [root,None] 
    res = [] 
    listNode=[]
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
        listNode.append(curr.val)
        total +=1
      else:
        res.append(listNode)
        listNode=[]
    res.append(listNode)
    return res
  
  
  def levelOrderBottom(self,root): 
    levelOrder = self.levelOrder(root) 
    res = deque()
    for lst in levelOrder:
      res.appendleft(lst)
    return res
    
print(Solution().levelOrderBottom(root))