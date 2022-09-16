
class Solution:
  def binarySearch (self,arr,target):
    low = 0 
    high = len(arr)-1 
    
    while low <= high: 
      mid = low+(high-low)>>1 
      
      if(arr[mid]==target):
        return mid 
      elif arr[mid]>target:
        high=mid-1 
      else:
        low=mid+1 
    return -1 
