class Solution:
  def searchMatrix(self,matrix,target):
    col_range = len(matrix[0])
    for row in range(len(matrix)):
      for col in range(col_range):
        if matrix[row][col]==target:
          return True 
    return False 
  
  def searchMatrix(self,matrix,target):
    n = len(matrix)
    col = len(matrix[0])
    row = 0 
    col = col-1 
    
    while col>=0 and row<n:
      
      if matrix[row][col] == target: 
        return True 
      
      if target > matrix[row][col]: 
        row+=1 
      else:
        col-=1 
        
    return False 
  
  def searchMatrix(self,matrix,target):
    
    col = len(matrix[0]) 
    low = 0 
    high = (len(matrix)*col)-1 
    
    while low<=high:
      mid = low+(high-low)//2 
      element = matrix[mid//col][mid%col] 
      if element==target:
        return True 
      elif target > element:
        low=mid+1 
      else:
        high=mid-1 
    return False 
  
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
is_present = Solution().searchMatrix
print(is_present(matrix,5))
    
 
    
    
    