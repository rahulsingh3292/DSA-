
from tree_data import root 
from collections import deque
class Solution:
  def bfs(self,root):
    row = [] 
    queue = deque()
    queue.append(root)
    mx=0 
    mn = root.data
    while queue:
        node = queue.popleft()
        mx = max(node.data,mx)
        mn = min(mn,node.data)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
    return (mn,mx)
    
  def findMax(self,root):
    return self.bfs(root)[1]
  def findMin(self,root):
    return self.bsf(root)[0]
  
  def dfs(self,root):
    if root is None:
      return 0
    return max(root.data,
    self.dfs(root.left),self.dfs(root.right))
 
print(Solution().dfs(root))