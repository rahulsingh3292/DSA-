class Solution: 
  def isPossible (self,arr,n,k):
    painter = 1 
    _sum = 0 
    for unit in arr:
      _sum+=unit 
      if _sum>n:
        painter+=1 
        _sum = unit 
      if painter>k: return False 
    return True 
      
  
  def findLargestMinDistance(self,arr,_n,k):
    n = len(arr)
    if n<k: return max(arr)
    
    low = max()
    high = sum(arr)
    while low<=high:
      mid = low+(high-low)//2 
  
      possible= self.isPossible(arr,mid,k) 
      if possible:
         ans = mid 
         high=mid-1 
      else:
        low=mid+1 
    return ans 

      
      
     