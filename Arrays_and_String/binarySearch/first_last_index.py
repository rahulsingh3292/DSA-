class Solution:
  def searchRange(self, arr: List[int], target: int) -> List[int]:
    low = 0 
    high = len(arr)-1 
    while low<=high:
      mid = low+(high-low)//2
      if arr[mid]==target:
        i,j = mid ,mid
        
        while i>0 and arr[i-1] == target:
          i-=1 
        while j<len(arr)-1 and arr[j+1]==target:
          j+=1 
        return i,j 
        
        
      elif arr[mid]>target:
        high=mid-1 
      else:
        low=mid+1 
    return (-1,-1)
  
  def solve(self,arr,target):
    return self.searchRange(arr,tar)