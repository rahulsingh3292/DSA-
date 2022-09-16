import math 
class Solution:
  def ceil(self,arr: list[int] ,target: int)-> int: 
    
    low = 0 
    high = len(arr) 
    while low<high:
      mid = low+(high-low)//2 
      
      if arr[mid] == target:
        return arr[mid] 
      elif arr[mid]<target:
        low=mid+1 
      else:
        high=mid 
    
    return -1 if high>=len(arr) else arr[high]
   