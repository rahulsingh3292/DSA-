class Solution:
  def getGrid(self,row,col):
    # return type => starting_row,endingRow,starting_col,endingCol
    if row <= 2:
      if col <= 2:
        return (0,3,0,3)  
      
      elif col<=5:
        return (0,3,3,6) 
      
      else:
        return (0,3,6,9) 
        
    if row<=5:
      if col <=2:
        return (3,6,0,3)
      elif col<=5:
        return (3,6,3,6) 
      else:
        return (3,6,6,9)
    
    if row<=8:
      if col<=2:
        return (6,9,0,3)
      elif col<=5:
        return (6,9,3,6)
      else:
        return (6,9,6,9)
  
  def isGridSafe(self,board,row,col,n):
    
    start_row,end_row,starting_col,ending_col=self.getGrid(row,col)
   
    for i in range (start_row,end_row):
      for j in range(starting_col,ending_col):
        if j==col: 
          continue
        if board[i][j]==n:
          return False 
    
    return True 
     
  def isSafe(self,board,i,j,n):
    # checking if 3*3 grid box is safe..
    if not self.isGridSafe(board,i,j,n):
      return False 
    
    # checking if row is safe.. 
    for k in range(9):
      if k == j:
        continue
      
      if board[i][k]==n:
        return False 
      
    # checking if colum is safe.. 
    for k in range(9):
      if k==i:
        continue
      if board[k][j]==n:
        return False
        
    return True  
  

  def isValid(self,board):
    for i in range(9):
      for j in range(9):
        n = board[i][j] 
        if n!=".":
          if not self.isSafe(board,i,j,n):
            return False 
    return True  
    
    
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValid(board))