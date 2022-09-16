
# Python 3 Solution 

from collections import deque
class Solution:
  # Time & Space complexity => O(N) - O(1) 
  def maximumSubArray(self,k,arr,n):
    i=j=0 
    sum=mx= 0 
    while j<n:
      sum += arr[j]
      if (j-i)+1 == k:
        mx = max(mx,sum)
        sum -=arr[i]
        i+=1
        
      j+=1 
    return mx 
  
  # Time & Space => O(N)- O(N) for Queue
  def maximumSubArrayK(self,k,arr,n):
    i=j=0 
    sum = 0 
    deq = deque()
    mx = 0
    while j<n:
      sum +=arr[j]
      deq.append(arr[j])
      if (j-i)+1 == k:
        minusVal = deq.popleft()
        mx = max(mx,sum)
        sum -=minusVal
        i+=1
      j+=1 
    return mx 
  
  # Time & Space => O(N*k) - O(1)
  def maxSubArrayK(self,k,arr,n):
    mx = 0 
    for i in range((n-k)+1):
      sum = 0 
      for j in range(i,i+k):
        sum +=arr[j]
      mx = max(mx,sum)
    return mx 
    
  

arr = [1,2,3,4,5] 
n = len(arr)
print(Solution().maximumSubArray(2,arr,n)) 




def getCombinationOfTarget(arr,target):
  arr.sort()
  sum = 0 
  combination = []
  for n in arr:
    sum +=n 
    combination.append(n)
    if sum == target:
      return combination 
    if sum > target:
      return "Target not found"
  



