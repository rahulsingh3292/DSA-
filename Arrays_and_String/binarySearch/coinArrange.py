"""
1-> start 0-> n 
2-> take middle number and sum it if sum less then given n then it's possible to make stair then save it...  and 
move to next (low=mid+1) .. else it's not possible then stay(set) high=mid to middle number.. and repeat...

"""

class Solution:
  
  def arrangeCoins(self,n: int)-> int:
    if n==1:  return 1 
    
    low=0 
    high = n 
    stairs = 0 
    while low<high:
      mid = low+(high-low)//2 
      
      _sum = (mid*mid)-mid)>>1)+mid 
      
      if _sum==n: return mid 
      
      elif _sum>n:
        high=mid 
      else:
        stairs = mid 
        low=mid+1 
    return stairs 