class Solution:
  def eualPairs(self,matrix):
    n = len(matrix)
    col_dict = {} 
    
    
    for row in range(n):
      col_data= list()
      for col in range(n):
        col_data.append(matrix[col][row])
      col_data=tuple(col_data)
      if col_data in col_dict:
        col_dict[col_data]+=1 
      else:
        
        col_dict[col_data]=1 
        
    count = 0
    for row in range(n):
      col_data = list()
      for col in range(n):
        col_data.append(matrix[row][col])
      col_data=tuple(col_data)
      if col_data in col_dict:
         count +=col_dict[col_data]
    return count 

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Solution().solve(grid)
  