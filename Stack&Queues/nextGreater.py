
from collections import deque 
class Solution:
  def nextGreaterElements(self,arr):
    n = len(arr)-1
    stack = deque() 
    res = [-1]*(n+1) 
    
    for k in range(2):
      for i in range(n,-1,-1):
        val = arr[i]
        if stack and stack[-1] > val:
          res[i] = stack[-1]
          stack.append(val)
        else:
          while stack and stack[-1]<=val:
            stack.pop()
          if stack:
            res[i] = stack[-1] 
          stack.append(val)
    return res 
    
arr = [1,2,1] 
Solution().nextGreaterElements(arr)