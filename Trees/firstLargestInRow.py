
from tree_data import root 
from collections import deque
class Solution:
  def bfs(self,root):
    row = [] 
    queue = deque()
    queue.append(root)
    while queue:
      count = len(queue)
      mx = float('-inf')
      while count >0:
        node = queue.popleft()
        mx = max(node.val,mx)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
        count -=1
      row.append(mx)
    return row
    
  def largestValues(self,root):
    return self.bfs(root)

print(Solution().largestValues(root))