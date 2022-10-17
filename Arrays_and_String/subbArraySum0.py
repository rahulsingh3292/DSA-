
class Solution:
  def subArrayExists(self,arr):
    n = len(arr)  
    data = {0:1} 
    sum = 0 
    for i in range(len(arr)):
      sum +=value
      if sum in data:
        return True 
      data[sum] = 1 
    return False 