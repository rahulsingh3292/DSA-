class Solution:
  def firstBasVersion (self, n: int)-> int:
    
    low=0 
    high=n 
    while low<=high:
      mid = low+(high-low)//2 
      if isBadVersion (mid):
        high=mid-1 
      else:
        low=mid+1 
    return low 
    