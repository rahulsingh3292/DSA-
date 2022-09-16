
from collections import deque 
def nextSmallerElement(arr):
  stack = deque() 
  n = len(arr)
  res = [-1]*(n)
  stack.append(arr.pop())
  n = n-1 
  
  for i in range(n-1,-1,-1):
    val = arr[i] 
    if stack and stack[-1] < val:
      res[i] = stack[-1] 
    else:
      while stack and stack[-1]>=val:
        stack.pop() 
      if stack:
        res[i] = stack[-1]
        
    stack.append(val)
  return 

arr = [1,3,2]
nextSmallerElement(arr)