class Solution: 
  def findMin(self,arr):
    low = 0 
    high=len(arr)-1 
    while low< high:
      mid = low+(high-low)//2 
      
     
      if arr[mid] > arr[high]:
        low=mid+1 
      elif arr[mid] < arr[high] :
        high=mid
      else:
        high-=1 
     
    return arr[low]
 

find = Solution().findMin 
arr= [3,3,3,3,3,2,2,0,1,3] 
print(find(arr))