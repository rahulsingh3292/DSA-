class Solution:
  def pairCount(self,spell,potions,req_success,n):
    # check for the last smallest index
    # whose product k*potions[index] which less than success.. 
    
    low = 0 
    high = n-1 
    
    while low<=high:
      mid = low+(high-low)//2 
      
      if spell*(potions[mid]) >= req_success:
        high=mid-1 
      else:
        low=mid+1 
    return 0 if low>=n else (((n-1)-low)+1)
    
  def successfulPairs(self,spell,potions,success):
    potions.sort() 
    n = len(potions)
    result = [self.pairCount(spell,potions,success,n) for spell in spells ]
    return result 
    
    
  
      
    
    
    
   