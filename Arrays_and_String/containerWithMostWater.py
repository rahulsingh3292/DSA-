class Solution:
  # Time Complexity => O(n^2) 
  def maxArea(self,height):
    n = len(height)
    maxWaterArea=0 
    for i in range(n-1):
      for j in range(i+1,n):
        maxWaterArea=max(maxWaterArea,min(height[i],height[j])*(j-i))
    return maxWaterArea 
   
  # TC => O(N)
  def maxArea(self,height):
    n = len(height)
    i,j,maxWaterArea=0,n-1,0

    while i<j:
      left_height = height[i] 
      right_height = height[j] 
      
      maxWaterArea = max(maxWaterArea,
      min(left_height,right_height)*(j-i))
      if left_height <= right_height:
        i+=1 
      if right_height <= left_height:
        j-=1 
    return maxWaterArea

    

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))