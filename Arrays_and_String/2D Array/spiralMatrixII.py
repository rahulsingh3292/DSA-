class Solution:
  def generateMatrix(self,n):
   
    total = n*n
    count=0 
    starting_row = 0 
    ending_row = n-1
    starting_col = 0 
    ending_col = n-1 
    
    result = [[0 for j in range(n)] for i in range(n)] 
    
    
    while count<total:
      
      for i in range(starting_row,ending_col+1):
        if count <total:
          count+=1 
          result[starting_row][i]=count
    
      starting_row+=1 

      for i in range(starting_row,ending_row+1):
        if count<total:
          count+=1 
          result[i][ending_row] = count
      ending_col-=1 
        
      for i in range(ending_col,starting_col-1,-1):
        if count<total:
          count+=1 
          result[ending_row][i] = count
      ending_row-=1 

      for i in range(ending_row,starting_row-1,-1):
        if count<total:
          count+=1 
          result[i][starting_col]=count
      starting_col+=1 
      
    return result 

 