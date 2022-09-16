
from collections import deque 

class Solution:
  def leftSmaller (self,arr):
    n = len(arr)
    stack = deque()
    res = [-1]
    stack.append(arr[0])
    
    for i in range(1,n):
      val = arr[i] 
      if  stack[-1] < val :

        res.append(stack[-1])
        stack.append(val) 
      else:
        while stack and stack[-1]>=val:
          stack.pop() 
        if not stack:
          res.append(-1)
        else:
          res.append(stack[-1])
        stack.append(val) 
    return res 
    
    
arr =[-1,6,6,6,6] 
Solution().leftSmaller(arr)