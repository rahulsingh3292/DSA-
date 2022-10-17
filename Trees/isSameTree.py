from tree_data import *
class Solution:
  def _isSameTree(self,p,q):
    if p is None and q is None: 
      return True 
    
    pl = p.left 
    pr = p.right 
    ql = q.left 
    qr = q.right 
    if (pl and not ql) or (not pl and ql):
      return False 
    
    if (pr and not qr) or (not pr and qr):
      return False 
    
    if p.val!=q.val:
      return False
   
    return self._isSameTree(p.left,q.left) and self._isSameTree(p.right,q.right)
  
  def isSameTree(self,p,q):
    if (p and not q) or (not p and q):
      return False 
    return self._isSameTree(p,q)
    
res = Solution().isSameTree(rootY,rootZ)
print(res)
     