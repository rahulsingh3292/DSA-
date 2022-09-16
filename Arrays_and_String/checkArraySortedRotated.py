class Solution:
  def isRotated(self,arr):
    count= 0 
    for i in range(0,len(arr)):
      if arr[i-1] > arr[i]:
        count+=1 
    
    if arr[-1] > arr[0]:
      count+=1 
    return count<=1 
    