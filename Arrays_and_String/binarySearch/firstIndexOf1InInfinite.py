class Solution:
  def binarySearch(self,arr: list[int],low: int, high: int)-> int:
    ans = -1 
    while low<=high:
      mid = low+(high-low)//2
      if arr[mid] == 1:
        ans = mid 
        high=mid-1 
      else:
        low=mid+1 
    return ans 
      
  def firstOne(self, arr:list[int])-> int:
    low=0 
    high = 1 
    while get(high) != 1 :
      low=high 
      high = high*2 
    return self.binarySearch(arr,low,high)
        

index = Solution().firstOne
arr = [0,0,1]
print(index(arr))
  
    