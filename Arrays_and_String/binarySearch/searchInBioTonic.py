# bioTonic array is array in starting 
# it highly increasing after a point it start decreasing... 


class Solution:
  def peak(self,arr):
    low = 0 
    high= len(arr)-1 
    while low<high:
      mid = low+(high-low)//2 
      if arr[mid] < arr[mid+1]:
        low=mid+1
      else:
        high=mid 
    return high
    
  def Bsearch(self,arr,low,high, target, is_rev=False):
    while low<=high:
      mid = low+(high-low)//2 
     
      if arr[mid] == target:
        return mid 
        
      elif arr[mid]>target:
        if is_rev:
          low=mid+1 
        else:
          high=mid-1 
        
      else:
        if is_rev:
          high=mid-1
        else:
          low=mid+1
    return -1 
  
  def searchInBiotonic(self, arr, target):
    peak= self.peak(arr) 
    
    left = self.Bsearch(arr,0,peak,target)
    right = self.Bsearch(arr,peak+1,len(arr)-1,target,True) 
    if left!= -1: return left 
    if right!= -1: return right 
    return -1
  
  def solve(self,arr,target):
    return self.searchInBiotonic(arr,target)