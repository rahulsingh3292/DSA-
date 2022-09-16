"""
  
   if index is even and value is odd 
   then search for odd index who's value is even.. swap them..
  
   if index is odd and value is even 
   then search for even index who's value is odd.. swap them.. 

  0 1 2 3 4 5 6 7
  1,2,4,5,6,8,9,3 => 1,2 
  2,1,4,5,6,8,9,3 => 8 ,9 
  2,1,4,5,6,9,8,3 

  
  0 1 2 3 4 5 6 7  
  1,9,5,3,2,4,6,8 => 1,4 
  4 9 5 3 2 1 6 8 => 5,8 
  4 9 8 3 2 1 6 5
     
"""


class Solution:
  def sortArrayByParityII(self,arr):
    
    def is_even(n):
      return n%2==0 
    
    i=0 
    n = len(arr)
    
    while i<n: 
      
      val = arr[i]
      
      while i+1 < n and (is_even(i) and is_even(val)) or (not is_even(i)) and (not is_even(val)):
        i+=1 
        
      if is_even(i) and (not is_even(val)):
        j = i+1
        while j<n:
          if is_even(arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
            break 
          j+=2 
        i+=1
        
      else:
        j = i+1 
        while j<n:
          if not is_even(arr[j]):
            (arr[i],arr[j]) = (arr[j],arr[i])
            break 
          j+=2 
        i+=1 
          
      
        
    return arr 
  
  

   
  
  
