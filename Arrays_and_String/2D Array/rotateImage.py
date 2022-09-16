class Solution:
  def rotate(self,arr):
    
   
   
    n = len(arr) 
    for i in range(n):
      for j in range(i+1):
        arr[i][j],arr[j][i] =arr[j][i],arr[i][j]
    
    for i in range(n):
      arr[i].reverse() 
    return arr 
      
      
arr = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(arr)