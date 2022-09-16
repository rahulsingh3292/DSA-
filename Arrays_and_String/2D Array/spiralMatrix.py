class Solution:
  def spiralOrder(self,arr):
    row = len(arr) 
    col = len(arr[0])
    total = row*col 
    count=0 
    
    starting_row = 0 
    ending_row = row-1 
    
    starting_col = 0 
    ending_col = col-1 
    
    result = [] 
    # spiral matrix col wise..
    while count<total:
     
      i = starting_row 
      while i<=ending_col and count<total:
        count+=1 
        val = arr[starting_row][i] 
        i+=1 
        result.append(val)
      starting_row +=1 
      
      i = starting_row 
      while i<=ending_row and count<total:
        count+=1 
        val = arr[i][ending_col] 
        result.append(val)
        i+=1 
      
      ending_col -=1 
        
      i = ending_col 
      while i>=starting_col and count<total:
        count+=1 
        val = arr[ending_row][i]
        result.append(val)
        i-=1 
      ending_row -=1 
      
      i = ending_row 
      while i>=starting_row and count<total:
        count+=1 
        val = arr[i][starting_col]
        result.append(val)
        i-=1
      starting_col +=1 
    return result
      
   
  # spiral matrix row wise.. 
  
  def spiralOrder(self,arr):
    n = len(arr) 
    col = len(arr[0])
    total = n*col
    
    starting_col = 0 
    starting_row = 0 
    
    ending_row =  n-1 
    ending_col = col-1 
    
    count = 0 

    while count<total :
      cond = count<total
      # up to down 
      i = starting_row
      while i<=ending_row and cond:
        count+=1
        print(arr[i][starting_col],end=" ")
        i+=1 
      starting_col+=1 
      
      # left to right 
      i = starting_col 
      while i <= ending_col and cond:
        count+=1 
        print(arr[ending_row][i],end=' ')
        i+=1 
      ending_row -=1 
      
      # down to up 
      i=ending_row 
      while i >= starting_row and cond:
        count+=1 
        print(arr[i][ending_col],end=" ")
        i-=1 
      ending_col -=1 
      
      
      # right to left 
      i = ending_col 
      while i>=starting_col and cond:
        count+=1 
        print(arr[starting_row][i],end=" ")
        i-=1 
      starting_row +=1
 
    
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]
]
Solution().spiralOrder(a)