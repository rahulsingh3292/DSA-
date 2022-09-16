class Solution:
  # oddOccur question... 
  def SingleNonDuplicate(self, arr: list[int])-> int : 
    low=0 
    high = len(arr)-1 
    n=len(arr)
    while low<=high:
      mid = low+(high-low)//2 
      
      if (mid==n-1) or (mid==0) or (mid==high) or (arr[mid]!=arr[mid+1] and arr[mid] != arr[mid-1])
        return arr[mid]
      
      
      elif arr[mid] == arr[mid+1]:
        right = (high- (mid+2))+1 
        if right>=n  or right<=0: 
          high=mid-1 
          
        elif right%2==1:
          low=mid+2 
        else:
          high=mid-1 
          
      elif arr[mid]==arr[mid-1]:
        left = ((mid-2)-low)+1 
 
        if left%2 == 1 and left>=0:
          high=mid-2 
        else:
          low=mid+1 
          
        
        
        
single = Solution().SingleNonDuplicate 
print(single([1,1,2,2,3,3,4,5,5,6,6,7,7]))
      
      