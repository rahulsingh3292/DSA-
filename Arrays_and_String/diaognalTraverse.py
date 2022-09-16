from typing import List 

class Solution:
  def __init__(self):
    self.up: bool = True 
    
  def solve(self,matrix: List[List[int]],i: int,j: int,n: int,res: List[int]):
    row_up,rowUpCol = i+1,j-1
    row_down,rowDownCol= i+1,j-1 
    
    if self.up:
      ans: List[int] = [matrix[i][j]] 
      while row_up<n and rowUpCol>=0:
        ans.append(matrix[row_up][rowUpCol])
        matrix[row_up][rowUpCol] = None
        row_up +=1 
        rowUpCol -=1  
      self.up = False 
      res.extend(reversed(ans))
      return 


    ans: List[int] = [matrix[i][j]] 
    while row_down<n and rowDownCol>=0:
      ans.append(matrix[row_down][rowDownCol])
      matrix[row_down][rowDownCol]=None
      rowDownCol -=1 
      row_down +=1
    self.up = True 
    res.extend(ans)
    return 
    
    
  def findDiagonalOrder(self,matrix: List[List[int]]):
    n,m = len(matrix),len(matrix[0]) 
    res: List[int] = [] 
    for i in range(n):
      for j in range(m):
        if matrix[i][j] != None:
          self.solve(matrix,i,j,n,res)
          matrix[i][j] = None

    return res 
    
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
res = Solution().findDiagonalOrder(matrix)
print(res)

