
def subarray(arr):
  n = len(arr) 
  for i in range(n):
    for j in range(i,n):
      curr = 0 
      for k in range(i,j+1):
        print(arr[k],end=" ") 
      print()
    print()


class Solution:
  def maxSubarray(self,arr):
    mx = float("-inf") 
    currSum = 0 
    for i in range(len(arr)):
      currSum +=arr[i] 
      
      if currSum>mx:
        mx = currSum
        
      if currSum < 0:
        currSum = 0 
    
    return mx 
    
print(Solution().maxSubarray([-1]))