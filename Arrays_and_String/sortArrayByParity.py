# algorithm dutch national flag.. 

class Solution:

  def sortArrayByParity(self,arr):
    def is_even(n):
       return (n&1)== 0
       
    n = len(arr) 
    left = 0 
    right = n-1 
   
    while left<right: 
      left_val = arr[left]
      right_val = arr[right] 
      
      if is_even(right_val) and (not is_even(left_val)):
      
        arr[right],arr[left] = left_val,right_val 
        left+=1 
        right-=1 
      
      elif (not is_even(left_val)) and (not is_even(right_val)):
        right-=1 
      
      else:
        left+=1
        
    return arr
      

      
  