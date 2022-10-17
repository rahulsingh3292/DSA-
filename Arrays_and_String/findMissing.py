
class Solution:
  def findMissing(self,arr):
    n = len(arr)
    map = {} 
    res = []
    for val in arr: map[val] = 1 
    for i in range (1,n+1):
      if map.get(i) is None:
        res.append(i)
    return res 
  
  def countSort(self,arr):
    n = len(arr)
    count = [0]*(n+1)
    count[0] = 1 
    for val in arr: count[val]=1 
    return [index for index in range(1,n+1) if count[index]==0]
  
          
   
 
 
