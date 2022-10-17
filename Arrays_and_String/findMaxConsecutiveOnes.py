class Solution:
  def findMaxConsecutiveOnes(self,arr):
    i=j=mx=0 
    n = len(arr)
    while j <n : 
      while j<n and arr[j]!=1:
        j=j+1 
      i=j 
      while j<n and arr[j]==1: 
        j=j+1 
      mx = max(mx,(j-i))
    return mx 
      
arr = [1,1,0,2,1,1,5,7,1,1]   
arr=[1]
arr=[0]
Solution().maxConsicutiveOnes(arr)