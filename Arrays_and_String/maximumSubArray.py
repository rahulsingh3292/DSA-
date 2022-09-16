
from collections import deque 
class Solution:
  def max_of_subarrays(self,arr,k):
    n = len(arr) 
    deq = deque()
    result = [] 
    i=j=0
    while j < n:
      while deq and arr[j]>arr[deq[-1]]:
        deq.pop()
      deq.append(j) 
      
      if (j-i)+1 == k:
        if i < deq[0]:
          result.append(arr[deq[0]]) 
        else:
          result.append(arr[deq.popleft()])
        i=i+1
      j+=1 
    return result
    
arr = list(map(int,input().split()))
k = 4
res = Solution().max_of_subarrays(arr,k)

print(res)