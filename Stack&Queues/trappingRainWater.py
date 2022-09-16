class Solution:
  def trappingWater(self,arr,n):
    
    
    left=[0]*n 
    left[0]=arr[0]
    for i in range(1,n):
      left[i] = max(left[i-1],arr[i])
    
    right=[0]*n 
    right[-1] = arr[-1]
    for i in range(n-2,-1,-1):
      right[i] = max(right[i+1],arr[i])
    
    ans = 0 
    for i in range(n):
      ans += min(left[i],right[i])-arr[i] 
    return ans 

arr = [3,0,0,2,0,4]
n = len(arr)
Solution().trap(arr,n)