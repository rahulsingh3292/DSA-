class Solution:
  def guessNumber(self,n: int)-> int:
    low = 0 
    high = n 
    while low<=high:
      mid = low+(high-low)//2 
      
      response = guess(mid) 
      if response==0:
        return mid 
      elif response== -1:
        high=mid-1 
      else:
        low=mid+1 
        
    