class Solution:
  def sumOfThree(self,n):
    low=0 
    high = n 
    while low<=high:
      mid = low+(high-low)//2 
      
      n1,n2,n3 = mid,mid+1,mid+2 
      sum = n1+n2+n3
      if sum == n:
        return (n1,n2,n3)
      elif sum > n:
        high=mid-1 
      else:
        low=mid+1 
    return () 
  
  def sumOfThree(self,n):
    mid = n//3 
    if mid-1+mid+mid+1 == n:
      return (mid-1,mid,mid+1)
    return ()