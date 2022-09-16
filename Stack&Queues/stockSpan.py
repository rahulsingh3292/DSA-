

from collections import deque 

class Solution:
  def calculatePrevLargest(self,arr,n):
    res = [-1]*n 
    stack = deque()
    stack.append(0)
    
    for i in range(1,n):
      currentDayVal = arr[i]
      
      if stack and arr[stack[-1]]>currentDayVal:
        res[i] = stack[-1]
      else:
        while stack and arr[stack[-1]]<=currentDayVal:
          stack.pop()
        if stack:
          res[i] = stack[-1] 
      stack.append(i)
    return res 
         
  def calculateSpan (self,arr,n):
    left = self.calculatePrevLargest(arr,n)
    result = [-1]*n 
    for index in range(n):
      result[index] = (index-left[index])
    return result
    
    
  
arr = [1,2,1,3,2,1,4,5,6,7,1,2,3,1,2,2,1,2,2,1,3,3,4,5,6 ]
n = len(arr)
res = Solution().calculateSpan(arr,n)
print(res)