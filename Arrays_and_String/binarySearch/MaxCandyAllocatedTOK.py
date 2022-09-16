
"""
# Q-> maximum candy allocated to k children .. 

1-> question asked that what the max candy you can give to all k child..

2-> choose the max candy from the array and start binary search.. 
3-> select middle of max ele and check weather it is possible to distribute

4-> loop->n and count+=n//given_candy  
if count >= k return True else return False 

if True then try for next_max_candy..

"""
class Solution:
  def possible(self,arr: list[int], candy: int,k: int )-> bool: 
    
    count = 0 
    for n in arr:
       count+=n//candy 
    if count>=k : return True 
    return False
    
  def maximumCandies(self, arr: list[int], k: int)-> int: 
    low: int = 0 
    high: int = max(arr) 
    candy: int = 1
    
    while low<=high:
      mid: int = low+(high-low)//2 

      if self.possible(arr,mid,k):
        candy = mid 
        low=mid+1 
      else:
        high=mid-1 
        
    return candy 

maxmimum = Solution().maximumCandies 
arr = [2,5]
print(maxmimum(arr,8))
    