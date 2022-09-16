from collections import deque 
class Solution:
  def left(self,arr,n):
    res = [-1]*n 
    stack = deque() 
    stack.append(0)
    for i in range (1,n):
      val = arr[i] 
      if stack and arr[stack[-1]]<val:
        res[i] = stack[-1]
      else:
        while stack and arr[stack[-1]]>=val:
          stack.pop()
        if stack:
          res[i] = stack[-1] 
      stack.append(i)
    return res 
      
    
  def right(self,arr,n):
    res=[n]*n 
    stack = deque()
    stack.append(n-1)
    for i in range(n-2,-1,-1):
      val = arr[i]
      if stack and arr[stack[-1]]<val:
        res[i] = stack[-1] 
      else:
        while stack and arr[stack[-1]]>=val:
          stack.pop() 
        if stack:
          res[i] = stack[-1] 
      stack.append(i)
    return res 
    
  def largestRectangleArea(self,height):
    n = len(height)
    left = self.left(height,n)
    right= self.right(height,n)
    maxArea = 0 
    for i in range(n):
      newArea = ((right[i]-left[i])-1)*(height[i])
      maxArea = max(maxArea,newArea)
    return maxArea 
    