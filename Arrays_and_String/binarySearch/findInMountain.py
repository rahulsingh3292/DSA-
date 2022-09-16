class Solution: 
  def findInMountainArray(self, target,mountain_arr)-> int:
    low = 0 
    high = mountain_arr.length()-1 
    
    while low<high:
      mid = low+(high-low)//2 
      
      if mountain_arr.get(mid)>mountain_arr(mid+1):
        high=mid 
      else:
        low=mid+1 
  
       
    _low = 0 
    _high = high
    
    # simple binary search...
    while _low<=_high:
      mid = _low+(_high-_low)//2 
      
      if mountain_arr.get(mid) ==target:
        return mid 
      
      elif mountain_arr.get(mid)>target:
        _high = mid-1
      else:
        _low=mid+1
  
    _low = high+1 
    _high = mountain_arr.length()-1
    
    # reverse binary Search... 
    while _low<=_high:
      mid = _low+(_high-_low)//2 
      
      if mountain_arr.get(mid) ==target:
        return mid 
      
      elif mountain_arr.get(mid)>target:
        _low=mid+1 
      else:
        _high=mid-1 
  
   return -1 

 
index = Solution().find 
arr = [1,2,10,2,3,5,10,2,3,4,]
#arr = [0,1,2,4,2,1]
print(index(arr,3))