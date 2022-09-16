

from collections import deque 
class Solution:
  def printFirstNegativeInteger(self,arr,n,k):
    result = [] 
    deq = deque()
    i=j=0 
    while j<n:
      val = arr[j] 
      if val<0:
        deq.append(j) 
      
      if (j-i)+1 == k:
        i +=1
        if not deq:
          result.append(0)
        elif i<=deq[0]:
          result.append(arr[deq[0]])
        else:
          result.append(arr[deq.popleft()])
      j +=1 
    
    return result 
 
 
arr =[-8, 2, 3, -6, 10]
n = len(arr) 
k = 2
Solution().printFirstNegativeInteger(arr,n,k)
